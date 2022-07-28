#!/usr/bin/python3

from bs4 import BeautifulSoup
import pandas as pd
import requests, wget, os, urllib.request, urllib.error, logging


start_date = '2022-01-25'
end_date = '2022-01-31'

url = 'https://embracedata.inpe.br/callisto/'

logging.basicConfig(
  filename = 'callisto_download.log',
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
  full_uri = range_date.strftime('%Y-%m-%d')
  return full_uri


def makeDir(path):
  base_dir = os.getcwd()
  os.makedirs(base_dir + '/data/' + path, exist_ok=True)


def listFD(url, ext_len, ext=''):
  page = requests.get(url).text
  soup = BeautifulSoup(page, 'html.parser')
  return [url + node.get('href') for node in soup.find_all('a') if node.get('href').startswith(ext, 0, ext_len)]


def downloadFiles():
  range_date = returnRangeOfDates(start_date, end_date)
  for day in range_date:
    year_m = day[0:4]
    month_m = day[5:7]
    day_m = day[8:10]
    dir_m = f'CXP/{year_m}/{month_m}/'
    url_m = url + dir_m
    file_match = f'INPE_{year_m}{month_m}{day_m}'

    error_message = 'No data from this date or invalid input stn/date'
    checkURL(url_m, error_message)

    files = listFD(url_m, len(file_match), file_match)
    if files != []:
      data_dir = f'callisto/{dir_m}'
      makeDir(data_dir)
      for f in files:
        logging.info(f)
        wget.download(f, 'data/' + data_dir)
    else:
      logging.info(f'No files match with "{file_match}" for stn/date "{dir_m}"')


if __name__ == '__main__':
  downloadFiles()
