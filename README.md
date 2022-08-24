# Downloading files from Space Weather Repository
[![](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/embrace-inpe/download_embracedata/blob/master/LICENSE)
[![](https://img.shields.io/badge/python-3-blue.svg)](https://www.python.org/)
[![](https://img.shields.io/badge/Version-1.0-yellow.svg)](https://github.com/embrace-inpe/download_embracedata)
[![](https://img.shields.io/badge/INPE-EMBRACE-orange.svg)](http://www2.inpe.br/climaespacial/portal/pt/)

This software download data from Embrace repository available in https://embracedata.inpe.br

Need Python >= 3.6 to work

Python is a multi platform language and easy to run in Windows, MacOS and Linux(Native).
Download and install the last stable version of Python in https://www.python.org/downloads/ .

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

After this enter in project folder and install dependencies with pip3 command:
```sh
pip3 install -r requirements.txt
```
After installing dependencies you should execute the script called “get_data.py” that is inside the folder that was made download “download_embracedata-master”.

The script “get_data.py” is the only one that needs to change to download data. The first part that is necessary to edit are the range of date, stations, filters and the extensions. Each 
instrument has a particularity.

Modify just the instrument you want to download data, leave others in the same way.

Follow the example each instrument:

## Callisto

date with format: YYYY-MM-DD

Modify the dates. In the example below the script will download between date 2022-01-15 and 2022-01-31.
```python
CALLISTO = { 
  'start_date': '2022-01-15',
  'end_date': '2022-01-31'
}
```
## IMAGER

date and station/filter with format: YYYY-MM-DD

all available stations: ['BJL', 'BV', 'CA', 'CP', 'CF', 'SMS']

all available filters: ['O6', 'OH', 'O6-DARK', 'OH-DARK']

It is necessary to modify the range of dates, stations and filters.

In the example below the script will download datas between date 2022-01-29 and 2022-01-31 of stations CA and CP with filters O6-DARK', 'OH-DARK. Always the stations and filters are separated by comma, with as example.
```python
IMAGER = {
  'start_date': '2022-01-29',
  'end_date': '2022-01-31',
  'stations': ['CA', 'CP'],
  'filters': ['O6-DARK', 'OH-DARK']
}
```

## IONOSONDE
date and station/extension with format: YYYY-DOY

DOY = day of the year

all available stations: ['BLJ03', 'BVJ03', 'CAJ2M', 'CGK21', 'FZA0M', 'SAA0K', 'SMK29']

all available extensions: ['.RSF', '.SAO', '.PNG', '.DFT', '.DVL', '.SKY' 'SAO.XML' 'MMM']

It is necessary to modify the range of days of year, stations and extensions.

In the example below the script will download datas between date 2020-02-04 and 2020-02-05 of station BLJ03 with extension .SAO.  Always the stations and extensions are separated by comma, as example.
```python
IONOSONDE = {
  'start_date': '2020-035',
  'end_date': '2020-036',
  'stations': ['BLJ03'],
  'extensions': ['.SAO']
}
```
It is possible find the day of year in this page: https://www.calendario-365.com.br/numeros-dos-dias/2020.html

## LIDAR
date and element with this format: YYYY-MM-DD

all available elements: ['Potassium', 'Sodium']

It is necessary to modify the range of dates and elements of files.
In the example below the script will download datas between the dates 2022-07-28 and 2022-07-30 of elements Potassium and Sodium . The elements are separated by comma, as example.
```python
LIDAR = {
  'start_date': '2022-07-28',
  'end_date': '2022-07-30',
  'elements': ['Potassium', 'Sodium']
}
```
## MAGNETOMETER
date and station whit format: YYYY-MM-DD

all available stations: ['ALF', 'ARA', 'CBA', 'CHI', 'CXP', 'EUS', 'JAT', 'MAN','MED',
                        'PAL', 'PVE', 'RGA', 'SJC', 'SLZ', 'SMS', 'STM', 'TCM', 'VSS']

It is necessary to modify the range of dates and stations.

In the example below the script will download datas between the dates 2022-02-03 and 2022-02-05 of stations ALF and ARA. Always the stations are separated by comma, as example.
```python
MAGNETOMETER = {
  'start_date': '2022-02-03',
  'end_date': '2022-02-05',
  'stations': ['ALF', 'ARA']
}
```
## SCINTILLATION
date and stations with format: YYYY-DOY

DOY = day of the year

all available stations: ['afl', 'alt', 'apu', 'bht', 'bhz', 'boa', 'bov', 'bsa', 'bsb',
                         'cba', 'chp', 'cpa', 'cub', 'dou', 'imp', 'ios', 'nta', 'pbr',
                         'pln', 'ppt', 'pvh', 'sjc', 'sjk', 'slz', 'sta', 'tfe']

It is necessary to modify the range of days of the year and stations.

In the example below the script will download datas between 2020-02-15 and 2020-02-16 of stations imp, ios, sjk .  Always the stations and extensions are separated by comma, as example.
```python
SCINTILLATION = {
  'start_date': '2021-046',
  'end_date': '2021-047',
  'stations': ['imp', 'ios', 'sjk']
}
```
It is possible find the day of year in this page: https://www.calendario-365.com.br/numeros-dos-dias/2021.html


The second part that need to modify is the final do file, follow: 

```python
...
def download_Files():
  get_data.Callisto(**CALLISTO)
  get_data.Imager(**IMAGER)
  get_data.Ionosonde(**IONOSONDE)
  get_data.Lidar(**LIDAR)
  get_data.Magnetometer(**MAGNETOMETER)
  get_data.Scintillation(**SCINTILLATION)
  ...
```
Each line begins with “get_data.instrument” to refer to a specific instrument. For examples:
```text
 get_data.Callisto(**CALLISTO) - make download data of Callisto
 get_data.Imager(**IMAGER) - make download data of Imageador
 get_data.Ionosonde(**IONOSONDE) - make download data of Ionosonde
 get_data.Lidar(**LIDAR) - make download data of data Lidar
 get_data.Magnetometer(**MAGNETOMETER) - make download data of Magnetometer
 get_data.Scintillation(**SCINTILLATION) - make download data of Scintillation.
```
You need to uncomment the line of instruments you want to download and make a comment in front of the line of the instruments that you will not download. The # character that is used to make comments.

The example below, the script will download data from Callisto and Imager and ignore the others. 

```python
...
def download_Files():
  get_data.Callisto(**CALLISTO)
  get_data.Imager(**IMAGER)
  #get_data.Ionosonde(**IONOSONDE)
  #get_data.Lidar(**LIDAR)
  #get_data.Magnetometer(**MAGNETOMETER)
  #get_data.Scintillation(**SCINTILLATION)
...
```
Running script:
```sh
python3 get_data.py
```
After running the script a log file with name "download_embracedata.log" and data dir with name "data" will be created in project dir.

Output log informations is describe bellow:

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
No folder match in embracedata repository. In this case no have data from ALF station of year 2022:
```sh
2022-08-19 17:11:06,INFO - HTTP Error 404: Not Found - No data from this date or invalid input stn/date: "https://embracedata.inpe.br/magnetometer/ALF/2022/"
```
Invalid date or wrong input range of dates. In this case the range of dates is wrong:
```sh
2022-08-22 10:59:04,INFO - Invalid date or start date is great than end date.
Your entry dates:
2022-02-29
2022-01-31
```
## License
MIT