#!/usr/bin/python3

from bs4 import BeautifulSoup
import pandas as pd
import requests, wget, os, urllib.request, urllib.error, logging


stn = 'CP'
start_date = '2021-01-01'
end_date = '2021-01-02'
filters = ['OH-DARK', 'O6-DARK', 'O5-DARK']

url = 'https://embracedata.inpe.br/imager/'


logging.basicConfig(
  filename = 'imager_download.log',
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
  full_uri = range_date.strftime(f'{stn}/%Y/{stn}_%Y_%m%d/')
  return full_uri


def makeDir(path):
  base_dir = os.getcwd()
  os.makedirs(base_dir + '/data/' + path, exist_ok=True)


def listFD(url, ft_len, ft=''):
  page = requests.get(url).text
  soup = BeautifulSoup(page, 'html.parser')
  return [url + node.get('href') for node in soup.find_all('a') if node.get('href').startswith(ft, 0, ft_len)]


def downloadFiles():
  range_date = returnRangeOfDates(start_date, end_date, stn)
  for day in range_date:
    error_message = 'No data from this date or invalid input stn/date'
    checkURL(url + day, error_message)

    data_dir = 'imager' + '/' + day
    makeDir(data_dir)

    for ft in filters:
      if listFD(url + day, len(ft), ft) == []:
        logging.info(f'No file match with filter "{ft}" for stn/date "{day}"')
      else:
        for file in listFD(url + day, len(ft), ft):
          logging.info(file)
          wget.download(file, 'data/' + data_dir)


if __name__ == '__main__':
  downloadFiles()
