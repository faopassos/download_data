# Downloading files from Space Weather Repository
[![](https://img.shields.io/badge/python-3-blue.svg)](https://www.python.org/)
[![](https://img.shields.io/badge/Version-1.0-yellow.svg)](https://github.com/embrace-inpe/download_embracedata)
[![](https://img.shields.io/badge/INPE-EMBRACE-orange.svg)](http://www2.inpe.br/climaespacial/portal/pt/)

This software download data from Embrace repository available in https://embracedata.inpe.br

Need Python >= 3.6 to work

Python is a multiplataform languague and easy running in Windows, MacOS and Linux(Native).
Download and install last stable version of Python in https://www.python.org/downloads/

After install check your version:
```sh
$ python3 -V
$ Python 3.8.10
```

Clone Embrace Data Repository from github with git:
```sh
$ git clone https://github.com/embrace-inpe/download_embracedata
```
Or download compress file (zip) in link https://github.com/embrace-inpe/download_embracedata/archive/refs/heads/master.zip

After this enter in project folder and install dependences with pip3 command:
```sh
pip3 install -r requirements.txt
```
After install dependences you can execute script to download data from Embrace repository.

This part of script get_data.py is describe bellow and you need to unconment line for respective isntrument you want to download and comment others instruments.
In this example the script will download data from Callisto and Imager and igonore others:

```python
...
def download_Files():
  get_data = Embrace_Data()
  get_data.Callisto(**CALLISTO)
  get_data.Imager(**IMAGER)
  #get_data.Ionosonde(**IONOSONDE)
  #get_data.Lidar(**LIDAR)
  #get_data.Magnetometer(**MAGNETOMETER)
  #get_data.Scintillation(**SCINTILLATION)
...
```

Every instrument have a dict to download data. Example of all instrument input available to download is describe bellow:

Instrument / Stations / Filters:

1. ### CALLISTO:
```text
only date with format:
YYYY-MM-DD
```
Callisto example:
```python
CALLISTO = { 
  'start_date': '2022-01-15',
  'end_date': '2022-01-31'
}
```
2. ### IMAGER:
```text
date and station/filter with format:
YYYY-MM-DD
all available stations: ['BJL', 'BV', 'CA', 'CP', 'CF', 'SMS']
all available filters: ['O6', 'OH', 'O6-DARK', 'OH-DARK']
```
Imager example:
```python
IMAGER = {
  'start_date': '2022-01-29',
  'end_date': '2022-01-31',
  'stations': ['CA', 'CP'],
  'filters': ['O6-DARK', 'OH-DARK']
}
```
3. ### IONOSONDE:
```text
date and station/extension with format:
YYYY-DOY
DOY = day of the year
all available stations: ['BLJ03', 'BVJ03', 'CAJ2M', 'CGK21', 'FZA0M', 'SAA0K', 'SMK29']
all available extensions: ['.RSF', '.SAO', '.PNG', '.DFT', '.DVL', '.SKY' 'SAO.XML' 'MMM']
```
Ionosonde example:
```python
IONOSONDE = {
  'start_date': '2020-035',
  'end_date': '2020-036',
  'stations': ['BLJ03', 'CAJ2M'],
  'extensions': ['.SAO', '.RSF']
}
```
4. ### LIDAR:
```text
date and element with this format:
YYYY-MM-DD
all available elements: ['Potassium', 'Sodium']
```
Lidar example:
```python
LIDAR = {
  'start_date': '2022-07-28',
  'end_date': '2022-07-30',
  'elements': ['Potassium', 'Sodium']
}
```
5. ### MAGNETOMETER:
```text
date and station whit format:
YYYY-MM-DD
all available stations: ['ALF', 'ARA', 'CBA', 'CHI', 'CXP', 'EUS', 'JAT', 'MAN','MED',
                        'PAL', 'PVE', 'RGA', 'SJC', 'SLZ', 'SMS', 'STM', 'TCM', 'VSS']
```
Magnetometer example:
```python
MAGNETOMETER = {
  'start_date': '2022-02-03',
  'end_date': '2022-02-05',
  'stations': ['ALF', 'ARA', 'SJC']
}
```
6. ### SCINTILLATION:
```text
date and stations with format:
YYYY-DOY
DOY = day of the year
all available stations: ['afl', 'alt', 'apu', 'bht', 'bhz', 'boa', 'bov', 'bsa', 'bsb',
                         'cba', 'chp', 'cpa', 'cub', 'dou', 'imp', 'ios', 'nta', 'pbr',
                         'pln', 'ppt', 'pvh', 'sjc', 'sjk', 'slz', 'sta', 'tfe']
```
Scintillation example:
```python
SCINTILLATION = {
  'start_date': '2021-046',
  'end_date': '2021-047',
  'stations': ['imp', 'ios', 'sjk']
}
```
Running script:
```sh
python3 get_data.py
```
After run script a log file with name "download_embracedata.log" and data dir with name "data" will be created in project dir.

Log output infos:

File download:
```sh
2022-08-19 17:11:09,INFO - Downloading file "ara03feb.22m" from "https://embracedata.inpe.br/magnetometer/ARA/2022/"
```
File already download and will not downloaded again:
```sh
2022-08-22 11:00:37,INFO - File "ara05feb.22m" already downloaded.
```
No file from specific date:
```sh
2022-08-19 17:11:08,INFO - No file match with name "alf05feb.22m" for stn/date "https://embracedata.inpe.br/magnetometer/ALF/2022/"
```
No folder match in embracedata repository. In this case no have data from ALF station and year 2022:
```sh
2022-08-19 17:11:06,INFO - HTTP Error 404: Not Found - No data from this date or invalid input stn/date: "https://embracedata.inpe.br/magnetometer/ALF/2022/"
```
Wrong input range of dates or date missing. In this case the range of dates is wrong:
```sh
2022-08-22 10:59:04,INFO - Invalid date or start date is great than end date.
Your entry dates:
2022-02-29
2022-01-31
```
## License

MIT
