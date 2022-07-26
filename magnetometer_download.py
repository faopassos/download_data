#!/usr/bin/python3

from bs4 import BeautifulSoup
import pandas as pd
import requests, wget, os, urllib.request, urllib.error, logging


stn = 'CXP'
start_date = '2020-01-01'
end_date = '2020-12-31'

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
  range_date = pd.date_range(start=start_date, end=end_date)
  full_uri = range_date.strftime('%Y%m%d%b')
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
  for rd in range_date:
    year = rd[0:4]
    month_m = f'{rd[8:11]}.{rd[2:4]}m'
    day = rd[6:8]
    full_uri = f'{url}{stn}/{year}/'
    files_m = f'{str(stn).lower()}{day}{month_m}'

    error_message = 'No data from this date or invalid input stn/date'
    checkURL(full_uri, error_message)

    files = listFD(full_uri, files_m)
    if files != []:
      data_dir = f'magnetometer/{stn}/{year}/'
      makeDir(data_dir)
      for f in files:
        logging.info(f)
        wget.download(f, 'data/' + data_dir)
    else:
      logging.info(f'No file match with name "{files_m}" for stn/date "{full_uri}"')


if __name__ == '__main__':
  downloadFiles()
