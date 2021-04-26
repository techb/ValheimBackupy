#!/usr/bin/env python3

from ftplib import FTP, all_errors
import configparser, sys, os


# function to handle possible errors I've been able to produce
def handleErrors(e, world=None):
    # Lower level network errors
    if e.__class__.__name__ == "TimeoutError":
        print("Timed out, check your host and port in config.ini")
        sys.exit()

    elif e.__class__.__name__ == "gaierror":
        print("Socket error, host address is wrong in config.ini")
        sys.exit()

    # it's an error with the ftp then
    else:
        err = str(e).split(None, 1)[0]
        if err == "530":
            print('Login Failed')
            sys.exit()

        if err == "550":
            print(f"World not found: {world}")
            return world


# get the config info from the ini file
config = configparser.ConfigParser()
config.read(r'config.ini')
usr = config['login']['usr']
pwd = config['login']['pwd']
host = config['server']['host']
port = int(config['server']['port']) # must be an int

# file extensions/types to download
ext = [".db", ".fwl", ".fwl.old"]
# list of files to delete if the world isn't found
deleteme = []


# get the list of worlds and strip any whitespace remove duplicates and empty elements
worlds = config['worlds']['world'].split(',')
for i in range(0, len(worlds)):
    worlds[i] = worlds[i].strip()
worlds = set(filter(None, worlds))


# setup the FTP connection
ftp = FTP()
try:
    ftp.connect(host, port)
except Exception as e:
    handleErrors(e)
try:
    ftp.login(usr, pwd)
except all_errors as e:
    handleErrors(e)


# switch to the worlds dir
ftp.cwd('.config/unity3d/IronGate/Valheim/worlds')
# loop through the worlds and download a backup file
for filename in worlds:
    for xt in ext:
        with open(f"backups/{filename}{xt}", "wb") as fp:
            try:
                ftp.retrbinary(f"RETR {filename}{xt}", fp.write)
                print(f"Received {filename}{xt}")
            except all_errors as e:
                d = handleErrors(e, filename+xt)
                if d:
                    deleteme.append(d)


# remove the worlds that were not found from the local backup folder
if len(deleteme) > 0:
    for f in deleteme:
        os.remove(f"backups/{f}")


# end
ftp.quit()