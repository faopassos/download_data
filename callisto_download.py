#!/usr/bin/python3

from bs4 import BeautifulSoup
import pandas as pd
import requests, wget, os, urllib.request, urllib.error, logging


start_date = '2022-02-01'
end_date = '2022-02-01'

url = 'https://embracedata.inpe.br/callisto/'

logging.basicConfig(
  filename = 'callisto_download.log',
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


def returnRangeOfDates(start_date, end_date):
  range_date = pd.date_range(start=start_date, end=end_date)
  full_uri = range_date.strftime('%Y-%m-%d')
  return full_uri


def listFD(url, ext_len, ext=''):
  page = requests.get(url).text
  soup = BeautifulSoup(page, 'html.parser')
  return [url + node.get('href') for node in soup.find_all('a') if node.get('href').startswith(ext, 0, ext_len)]


def downloadFiles():
  range_date = returnRangeOfDates(start_date, end_date)
  for rd in range_date:
    year = rd[0:4]
    month = rd[5:7]
    remote_dir = f'CXP/{year}/{month}/'
    full_url = url + remote_dir
    file_match = f'INPE_{year}{month}{rd[8:10]}'

    checkURL(full_url)

    files = listFD(full_url, len(file_match), file_match)
    if files != []:
      local_file_path = f'{os.getcwd()}/data/callisto/' + remote_dir
      os.makedirs(local_file_path, exist_ok=True)
      for file in files:
        file_exists = file.rsplit('/', 1)[1]
        if not os.path.exists(local_file_path + file_exists):
          try:
            logging.info(f'Downloading {file}')
            wget.download(file, local_file_path)
          except:
            logging.info(f'Something went wrong with file "{file}". Please try again later.')
        else:
          logging.info(f'File "{file_exists}" already downloaded.')
    else:
      logging.info(f'No files match with "{file_match}" for stn/date "{remote_dir}"')


if __name__ == '__main__':
  downloadFiles()
