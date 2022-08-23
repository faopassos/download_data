from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import requests, wget, os, urllib.request, urllib.error, logging


class Embrace_Data:
  def __init__(self):
    self.base_url = 'https://embracedata.inpe.br/'

    logging.basicConfig(
    filename = 'download_embracedata.log',
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
      if instrument == 'callisto' or instrument == 'imager' or instrument == 'magnetometer' or instrument == 'lidar':
        s_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        e_date = datetime.strptime(end_date, '%Y-%m-%d').date()
      elif instrument == 'ionosonde' or instrument == 'scintillation':
        s_date = datetime.strptime(start_date, '%Y-%j').date()
        e_date = datetime.strptime(end_date, '%Y-%j').date()
      if (s_date > e_date):
        exit()
      if instrument == 'callisto' or instrument == 'imager' or instrument == 'lidar':
        range_date = pd.date_range(start=start_date, end=end_date).strftime('%Y-%m-%d')
      elif instrument == 'ionosonde' or instrument == 'scintillation':
        range_s = datetime.strptime(start_date, '%Y-%j').strftime("%Y-%m-%d")
        range_e = datetime.strptime(end_date, '%Y-%j').strftime("%Y-%m-%d")
        range_date = pd.date_range(start=range_s, end=range_e).strftime('%Y-%j')
      elif instrument == 'magnetometer':
        range_date = pd.date_range(start=start_date, end=end_date).strftime('%Y%m%d%b')
      return range_date
    except:
      logging.info(f'Invalid date or start date is great than end date.\nYour entry dates:\n{start_date}\n{end_date}')
      exit()

  def listFiles(self, instrument, url, ext='', ext_len=0):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    if instrument == 'callisto' or instrument == 'imager' or instrument == 'lidar' or instrument == 'scintillation':
      return [url + node.get('href') for node in soup.find_all('a') if node.get('href').startswith(ext, 0, ext_len)] 
    elif instrument == 'ionosonde' or instrument == 'magnetometer':
      return [url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

  def Callisto(self, start_date, end_date):
    range_date = self.returnRangeOfDates('callisto', start_date, end_date)
    for rd in range_date:
      year = rd[0:4]
      month = rd[5:7]
      uri = f'callisto/CXP/{year}/{month}/'
      full_url = self.base_url + uri
      file_match = f'INPE_{year}{month}{rd[8:10]}'
      self.checkURL(full_url)

      files = self.listFiles('callisto', full_url, file_match, len(file_match))
      if files != []:
        local_file_path = f'{os.getcwd()}/data/' + uri
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
        logging.info(f'No files match with "{file_match}" for stn/date "{uri}"')

  def Imager(self, start_date, end_date, stations, filters):
    for stn in stations:
      range_date = self.returnRangeOfDates('imager', start_date, end_date)
      for rd in range_date:
        year = rd[0:4]
        month = rd[5:7]
        day = rd[8:10]
        uri = f'imager/{stn}/{year}/{stn}_{year}_{month}{day}/'
        self.checkURL(self.base_url + uri)
        for ft in filters:
          files = self.listFiles('imager', self.base_url + uri, ft, len(ft))
          if files != []:
            local_file_path = f'{os.getcwd()}/data/' + uri
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

  def Ionosonde(self, start_date, end_date, stations, extensions):
    for stn in stations:
      range_date = self.returnRangeOfDates('ionosonde', start_date, end_date)
      for rd in range_date:
        year = rd[0:4]
        doy = rd[5:8]
        uri = f'ionosonde/{stn}/{year}/{doy}/'
        self.checkURL(self.base_url + uri)

        for ext in extensions:
          files = self.listFiles('ionosonde', self.base_url + uri, ext)
          if files != []:
            local_file_path = f'{os.getcwd()}/data/' + uri
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
            logging.info(f'No file match with extension "{ext}" for stn/date "{uri}"')

  def Lidar(self, start_date, end_date, elements):
    range_date = self.returnRangeOfDates('lidar', start_date, end_date)
    for element in elements:
      for rd in range_date:
        year = rd[0:4]
        month = rd[5:7]
        day = rd[8:10]
        uri = f'lidar/{year}/{year}{month}{day}/{element}/'
        full_url = self.base_url + uri
        file_match = f'SJC_LID01_L0_{element[0:1]}RW_STP_V01_{year}{month}{day}'
        self.checkURL(full_url)

        files = self.listFiles('lidar', full_url, file_match, len(file_match))
        if files != []:
          local_file_path = f'{os.getcwd()}/data/' + uri
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
          logging.info(f'No files match with "{file_match}" for stn/date "{uri}"')
  
  def Magnetometer(self, start_date, end_date, stations):
    for stn in stations:
      range_date = self.returnRangeOfDates('magnetometer', start_date, end_date)
      for rd in range_date:
        year = rd[0:4]
        uri = f'magnetometer/{stn}/{year}/'
        full_url = self.base_url + uri
        self.checkURL(full_url)
        
        file_match = str(f'{stn}{rd[6:8]}{rd[8:11]}.{rd[2:4]}m').lower()
        local_file_path = f'{os.getcwd()}/data/magnetometer/{stn}/{year}/'

        if not os.path.exists(local_file_path + file_match):
          files = self.listFiles('magnetometer', full_url, file_match)
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

  def Scintillation(self, start_date, end_date, stations):
    for stn in stations:
      range_date = self.returnRangeOfDates('scintillation', start_date, end_date)
      for rd in range_date:
        rd_formated = datetime.strptime(rd, '%Y-%j').strftime("%Y-%m-%d")
        year = rd[0:4]
        doy = rd[5:8]
        month = rd_formated[5:7]
        day = rd_formated[8:10]
        uri = f'scintillation/{year}/{doy}/{stn}/'
        file_match = f'{stn}_{year}-{month}-{day}'
        self.checkURL(self.base_url + uri)

        files = self.listFiles('scintillation', self.base_url + uri, file_match, len(file_match))
        if files != []:
          local_file_path = f'{os.getcwd()}/data/' + uri
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
          logging.info(f'No file match with "{file_match}" for stn/date "{uri}"')
