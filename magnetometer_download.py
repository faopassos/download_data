#!/usr/bin/python3

from bs4 import BeautifulSoup
import pandas as pd
import requests, wget, os, urllib.request, urllib.error, logging


stn = 'EUS'
start_date = '2013-06'
end_date = '2013-07'

url = 'https://embracedata.inpe.br/magnetometer/'

logging.basicConfig(
  filename = 'magnetometer_download.log',
  format='%(asctime)s,%(levelname)s - %(message)s',
  datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO
)

def checkURL(url, message):
  try:
    urllib.request.urlretrieve(url)
  except urllib.error.HTTPError as err:
      logging.info(f'{err} - {message}: "{url}"')
      exit()


def returnRangeOfDates(start_date, end_date):
  range_date = pd.date_range(start=start_date, end=end_date, freq='MS')
  full_uri = range_date.strftime('%Y%m%b')
  return full_uri.str.lower()


def makeDir(path):
  base_dir = os.getcwd()
  os.makedirs(base_dir + '/data/' + path, exist_ok=True)


def listFD(url, ext=''):
  page = requests.get(url).text
  soup = BeautifulSoup(page, 'html.parser')
  return [url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]


def downloadFiles():
  range_date = returnRangeOfDates(start_date, end_date)
  for month in range_date:
    year = month[0:4]
    month_and_stn_match = f'{month[6:9]}.{month[2:4]}m' 
    full_uri = f'{url}{stn}/{year}/'
    error_message = 'No data from this date or invalid input stn/date'
    checkURL(full_uri, error_message)
    
    data_dir = f'magnetometer/{stn}/{year}/'
    makeDir(data_dir)

    if listFD(full_uri, month_and_stn_match) == []:
      logging.info(f'No file match with month "{month_and_stn_match}" for stn/date "{full_uri}"')
    else:
      for file in listFD(full_uri, month_and_stn_match):
        logging.info(file)
        wget.download(file, 'data/' + data_dir)


if __name__ == '__main__':
  downloadFiles()
