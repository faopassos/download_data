#!/usr/bin/python3

from bs4 import BeautifulSoup
import pandas as pd
import requests, wget, os, urllib.request, urllib.error, logging, datetime


stn = 'CXP'
start_date = '2022-06-01'
end_date = '2022-06-02'
extensions = ['m', '.TEST']

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


def returnRangeOfDates(start_date, end_date, stn):
  range_date = pd.date_range(start=start_date, end=end_date)
  full_uri = range_date.strftime(f'/%Y/{stn}%d%b.%ym')
  return stn + full_uri.str.lower()


def makeDir(path):
  base_dir = os.getcwd()
  os.makedirs(base_dir + '/data/' + path, exist_ok=True)


def listFD(url, ext=''):
  page = requests.get(url).text
  soup = BeautifulSoup(page, 'html.parser')
  return [url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]


def downloadFiles():
  range_date = returnRangeOfDates(start_date, end_date, stn)
  for day in range_date:
    error_message = 'No data from this date or invalid input stn/date'
    checkURL(url + day, error_message)

    data_dir = 'magnetometer' + '/' + day
    makeDir(data_dir)

    for ext in extensions:
      if listFD(url + day, ext) == []:
        logging.info(f'No file match with filter "{ext}" for stn/date "{day}"')
      else:
        for file in listFD(url + day, ext):
          logging.info(file)
          #wget.download(file, 'data/' + data_dir)


if __name__ == '__main__':
  downloadFiles()
