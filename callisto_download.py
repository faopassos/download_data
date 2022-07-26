#!/usr/bin/python3

from bs4 import BeautifulSoup
import pandas as pd
import requests, wget, os, urllib.request, urllib.error, logging


start_date = '2022-05-01'
end_date = '2022-05-02'

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


def returnRangeOfDates(start_date, end_date, stn):
  range_date = pd.date_range(start=start_date, end=end_date)
  full_uri = range_date.strftime(f'{stn}/%Y/%m/')
  return full_uri


def makeDir(path):
  base_dir = os.getcwd()
  os.makedirs(base_dir + '/data/' + path, exist_ok=True)


def listFD(url, ext=''):
  page = requests.get(url).text
  soup = BeautifulSoup(page, 'html.parser')
  return [url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]


def downloadFiles():
  range_date = returnRangeOfDates(start_date, end_date, 'CXP')
  for day in range_date:
    error_message = 'No data from this date or invalid input stn/date'
    checkURL(url + day, error_message)

    files = listFD(url + day, '.fit')
    if files != []:
      data_dir = f'callisto/{day}'
      makeDir(data_dir)
      for f in files:
        logging.info(f)
        wget.download(f, 'data/' + data_dir)
    else:
      logging.info(f'No files match with "{files}" for stn/date "{day}"')


if __name__ == '__main__':
  downloadFiles()
