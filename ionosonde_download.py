#!/usr/bin/python3

from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import requests, wget, os, urllib.request, urllib.error, logging


stations = ['CAJ2M', 'CGK21']
start_date = '2022-010'
end_date = '2022-010'
extensions = ['.SAO', '.PNG']

url = 'https://embracedata.inpe.br/ionosonde/'

logging.basicConfig(
  filename = 'ionosonde_download.log',
  format='%(asctime)s,%(levelname)s - %(message)s',
  datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO
)

def checkURL(url):
  try:
    urllib.request.urlretrieve(url)
  except urllib.error.HTTPError as err:
    message = 'No data from this date or invalid input stn/date'
    logging.info(f'{err} - {message}: "{url}"')
    #exit()


def returnRangeOfDates(start_date, end_date, stn):
  range_s = datetime.strptime(start_date, '%Y-%j').strftime("%Y-%m-%d")
  range_e = datetime.strptime(end_date, '%Y-%j').strftime("%Y-%m-%d")
  range_date = pd.date_range(start=range_s, end=range_e)
  full_uri = range_date.strftime(f'{stn}/%Y/%j/')
  return full_uri


def listFD(url, ext=''):
  page = requests.get(url).text
  soup = BeautifulSoup(page, 'html.parser')
  return [url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]


def downloadFiles():
  for stn in stations:
    range_date = returnRangeOfDates(start_date, end_date, stn)
    for rd in range_date:
      checkURL(url + rd)

      for ext in extensions:
        files = listFD(url + rd, ext)
        if files != []:
          local_file_path = f'{os.getcwd()}/data/ionosonde/' + rd
          os.makedirs(local_file_path, exist_ok=True)
          for file in files:
            file_exists = file.rsplit('/', 1)[1]
            if not os.path.exists(local_file_path + file_exists):
              try:
                logging.info(f'Downloading file {file}')
                wget.download(file, local_file_path)
              except:
                logging.info(f'Something went wrong with file "{file}". Please try again later.')
            else:
              logging.info(f'File "{file_exists}" already downloaded.') 
        else:
          logging.info(f'No file match with extension "{ext}" for stn/date "{rd}"')


if __name__ == '__main__':
  downloadFiles()
