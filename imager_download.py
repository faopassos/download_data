#!/usr/bin/python3

from bs4 import BeautifulSoup
import pandas as pd
import requests, wget, os, urllib.request, urllib.error, logging


# all available stations:
#stations = ['BJL', 'BV', 'CA', 'CP', 'SMS']
stations = ['BJL', 'CA', 'CP']

#Range of dates - YYYY-MM-DD
start_date = '2022-03-01'
end_date = '2022-03-01'

#All available filters
#filters = ['O6', 'OH', 'O6-DARK', 'OH-DARK']
filters = ['O6-DARK', 'OH-DARK']

url = 'https://embracedata.inpe.br/imager/'

logging.basicConfig(
  filename = 'imager_download.log',
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
  range_date = pd.date_range(start=start_date, end=end_date)
  full_uri = range_date.strftime(f'{stn}/%Y/{stn}_%Y_%m%d/')
  return full_uri


def listFD(url, ft_len, ft=''):
  page = requests.get(url).text
  soup = BeautifulSoup(page, 'html.parser')
  return [url + node.get('href') for node in soup.find_all('a') if node.get('href').startswith(ft, 0, ft_len)]


def downloadFiles():
  for stn in stations:
    range_date = returnRangeOfDates(start_date, end_date, stn)
    for rd in range_date:
      checkURL(url + rd)

      for ft in filters:
        files = listFD(url + rd, len(ft), ft)
        if files != []:
          local_file_path = f'{os.getcwd()}/data/imager/' + rd
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
          logging.info(f'No file match with filter "{ft}" for stn/date "{rd}"')


if __name__ == '__main__':
  downloadFiles()
