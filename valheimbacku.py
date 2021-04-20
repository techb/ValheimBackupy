#!/usr/bin/env python3

from ftplib import FTP
import configparser


# get the config info from the ini file
config = configparser.ConfigParser()
config.read(r'config.ini')
usr = config['login']['usr']
pwd = config['login']['pwd']
host = config['server']['host']
port = int(config['server']['port']) # must be an int

# get the list of worlds and strip any whitespace
worlds = config['worlds']['world'].split(',')
for i in range(0, len(worlds)):
    worlds[i] = worlds[i].strip()

# setup the FTP connection and switch to the worlds dir
ftp = FTP()
ftp.connect(host, port)
ftp.login(usr, pwd)
ftp.cwd('.config/unity3d/IronGate/Valheim/worlds')

# loop through the worlds and download a backup file
for filename in worlds:
    with open('backups/'+filename+'.db', 'wb') as fp:
        ftp.retrbinary('RETR '+filename+'.db', fp.write)

    with open('backups/'+filename+'.fwl', 'wb') as fp:
        ftp.retrbinary('RETR '+filename+'.fwl', fp.write)

    # Might get errors with a fresh server, haven't tested
    with open('backups/'+filename+'.fwl.old', 'wb') as fp:
        ftp.retrbinary('RETR '+filename+'.fwl.old', fp.write)

# end
ftp.quit()