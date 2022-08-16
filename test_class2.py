#!/usr/bin/python3
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import requests, wget, os, urllib.request, urllib.error, logging


class Embrace_Data:
  def __init__(self):
    self.base_url = 'https://embracedata.inpe.br/'

    logging.basicConfig(
    filename = 'embracedata_download.log',
    format='%(asctime)s,%(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO
    )

  def checkURL(self, url):
      try:
        urllib.request.urlretrieve(url)
      except urllib.error.HTTPError as err:
        message = 'No data from this date or invalid input stn/date'
        logging.info(f'{err} - {message}: "{url}"')

  def returnRangeOfDates(self, instrument, start_date, end_date):  
      try:
        if instrument == 'callisto' or instrument == 'imager':
          range_date = pd.date_range(start=start_date, end=end_date).strftime('%Y-%m-%d')
        elif instrument == 'ionossonde':
          range_s = datetime.strptime(start_date, '%Y-%j').strftime("%Y-%m-%d")
          range_e = datetime.strptime(end_date, '%Y-%j').strftime("%Y-%m-%d")
          range_date = pd.date_range(start=range_s, end=range_e).strftime('%Y-%j')
        elif instrument == 'magnetometer':
          range_date = pd.date_range(start=start_date, end=end_date).strftime('%Y%m%d%b')
        return range_date
      except:
        logging.info(f'Invalid date/range of dates!\n\nYour entry dates:\n{start_date}\n{end_date}')

  def listFiles(self, instrument, url, ext_len, ext=''):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    if instrument == 'callisto' or instrument == 'imager':
      return [url + node.get('href') for node in soup.find_all('a') if node.get('href').startswith(ext, 0, ext_len)]
    elif instrument == 'ionosonde' or instrument == 'magnetometer':
      return [url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

  def Callisto(self, start_date, end_date):
    range_date = self.returnRangeOfDates('callisto', start_date, end_date)
    for rd in range_date:
      year = rd[0:4]
      month = rd[5:7]
      remote_dir = f'CXP/{year}/{month}/'
      full_url = self.base_url + 'callisto/' + remote_dir
      file_match = f'INPE_{year}{month}{rd[8:10]}'

    self.checkURL(full_url)

    files = self.listFiles('callisto', full_url, len(file_match), file_match)
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

  def Imager(self, start_date, end_date):
    stations = ['BJL', 'CA', 'CP']
    filters = ['O6-DARK', 'OH-DARK']
    for stn in stations:
      range_date = self.returnRangeOfDates('imager', start_date, end_date)
      for rd in range_date:
        year = rd[0:4]
        month = rd[5:7]
        day = rd[8:10]
        uri = f'imager/{stn}/{year}/{stn}_{year}_{month}{day}/'
        self.checkURL(self.base_url + uri)
        for ft in filters:
          files = self.listFiles('imager', self.base_url + uri, len(ft), ft)
          if files != []:
            local_file_path = f'{os.getcwd()}/data/imager/' + uri
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
            logging.info(f'No file match with filter "{ft}" for stn/date "{uri}"')

download = Embrace_Data()
#download.Callisto('2022-01-31', '2022-01-31')
#download.Imager('2022-03-01', '2022-03-02')
