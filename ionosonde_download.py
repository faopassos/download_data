#!/usr/bin/python3

from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import requests, wget, os, urllib.request, urllib.error, logging


stn = 'CAJ2M'
start_date = '2022-010'
end_date = '2022-010'
extensions = ['.SAO', '.PNG']

url = 'https://embracedata.inpe.br/ionosonde/'

logging.basicConfig(
  filename = 'ionosonde_download.log',
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
  range_s = datetime.strptime(start_date, '%Y-%j').strftime("%Y-%m-%d")
  range_e = datetime.strptime(end_date, '%Y-%j').strftime("%Y-%m-%d")
  range_date = pd.date_range(start=range_s, end=range_e)
  full_uri = range_date.strftime(f'{stn}/%Y/%j/')
  return full_uri


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

    for ext in extensions:
      files = listFD(url + day, ext)
      if files != []:
        data_dir = f'ionossonde/{day}'
        makeDir(data_dir)
        for f in files:
          logging.info(f)
          wget.download(f, 'data/' + data_dir)  
      else:
        logging.info(f'No file match with extension "{ext}" for stn/date "{day}"')


if __name__ == '__main__':
  downloadFiles()
