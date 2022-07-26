#!/usr/bin/python3

from bs4 import BeautifulSoup
import pandas as pd
import requests, wget, os, urllib.request, urllib.error, logging


stn = 'SMS'
start_date = '2021-01-01'
end_date = '2021-02-28'

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
    files = f'{str(stn).lower()}{day}{month_m}'

    error_message = 'No data from this date or invalid input stn/date'
    checkURL(full_uri, error_message)

    if listFD(full_uri, files) == []:
      logging.info(f'No file match with name "{files}" for stn/date "{full_uri}"')
    else:
      data_dir = f'magnetometer/{stn}/{year}/'
      makeDir(data_dir)
      for file in listFD(full_uri, files):
        logging.info(file)
        wget.download(file, 'data/' + data_dir)


if __name__ == '__main__':
  downloadFiles()
