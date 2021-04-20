# ValheimBackupy
Python script to backup your worlds from the dedicated cloud gaming servers g-portal.com. Utilizes a cronjob to backup yout files at a specified tame every day.

## Install
- Visit {github url}
- Download code as zip
- Extract the folder

#### Command line
- `$ git clone {github url}`
- `$ cd ValheimBackupy`

## Config
- Create a new file in `ValheimBackupy/` called `config.ini`
- Copy the contents of `example.config.ini` into the new `config.ini` file
- Replace the information obtained from your g-portal.com account
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
  - {image of crontab -e}