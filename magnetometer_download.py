#!/usr/bin/python3

from bs4 import BeautifulSoup
import pandas as pd
import requests, wget, os, urllib.request, urllib.error, logging


#stations = ['ALF', 'ARA', 'CBA', 'CHI', 'CXP', 'EUS', 'JAT', 'MAN','MED',
#            'PAL', 'PVE', 'RGA', 'SJC', 'SLZ', 'SMS', 'STM', 'TCM', 'VSS']

stations = ['ALF', 'ARA', 'CBA']

start_date = '2015-01-01'
end_date = '2015-01-10'

url = 'https://embracedata.inpe.br/magnetometer/'

logging.basicConfig(
  filename = 'magnetometer_download.log',
  format='%(asctime)s,%(levelname)s - %(message)s',
  datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO
)

def checkURL(url):
  try:
    urllib.request.urlretrieve(url)
  except urllib.error.HTTPError as err:
    message = 'No data from this date or invalid input stn/date'
    logging.info(f'{err.code} - {message}: "{url}"')
    #exit()


def returnRangeOfDates(start_date, end_date):
  try:
    dataset = pd.date_range(start=start_date, end=end_date)
    dataset_formated = dataset.strftime('%Y%m%d%b')
    return dataset_formated.str.lower()
  except:
    logging.info(f'Invalid date/range of dates!\n\nYour entry dates:\n{start_date}\n{end_date}')
    exit()


def listOfFiles(url, ext=''):
  page = requests.get(url).text
  soup = BeautifulSoup(page, 'html.parser')
  return [url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]


def downloadFiles():
  for stn in stations:
    range_date = returnRangeOfDates(start_date, end_date)
    for rd in range_date:
      year = rd[0:4]
      full_url = f'{url}{stn}/{year}/'
      checkURL(full_url)
      
      file_match = f'{str(stn).lower()}{rd[6:8]}{rd[8:11]}.{rd[2:4]}m'
      local_file_path = f'{os.getcwd()}/data/magnetometer/{stn}/{year}/'

      if not os.path.exists(local_file_path + file_match):
        files = listOfFiles(full_url, file_match)
        if files != []:
          os.makedirs(local_file_path, exist_ok=True)
          for file in files:
            try:
              logging.info(f'Downloading file "{file_match}" from "{full_url}"')
              wget.download(file, local_file_path)
            except:
              logging.info(f'Something went wrong with file "{file_match}". Please try again later.')
        else:
          logging.info(f'No file match with name "{file_match}" for stn/date "{full_url}"')
      else:
        logging.info(f'File "{file_match}" already downloaded.')


if __name__ == '__main__':
  downloadFiles()
