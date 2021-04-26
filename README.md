# ValheimBackupy
Python script to backup your worlds from the dedicated cloud gaming servers g-portal.com. Utilizes a cronjob to backup your files at a specified time every day.

## Install
- Visit https://github.com/techb/ValheimBackupy
- Download code as zip
- Extract the folder

#### Command line
- `$ git clone git@github.com:techb/ValheimBackupy.git`
- `$ cd ValheimBackupy`

## Config
- Create a new file in `ValheimBackupy/` called `config.ini`
- Copy the contents of `example.config.ini` into the new `config.ini` file
- Replace the information obtained from your g-portal.com account
  - Log into g-portal and select your Velheim server, the information you need will look similar to this:
  ![g-portal](/img/g-portal.png)
- Save the file
#### Command line
- `$ cp example.config.ini config.ini`
- `$ vim config.ini`
    - `... edit file, save and quit ...`


## Run
- `$ chmod +x valheimbacku.py`
- `$ crontab -e`
  - Create cron job
  - `20 4 * * * /<Path To Script>/valheimbacku.py`

![crontab](/img/crontab.png#1)