#!/usr/bin/python3
from subprocess import call
from bs4 import BeautifulSoup
import pandas as pd
import requests, wget, os, urllib.request, urllib.error, logging


class EmbraceData:
  def __init__(self, instrument, start_date, end_date):
    self.instrument = instrument
    self.start_date = start_date
    self.end_date = end_date
    self.base_url = 'https://embracedata.inpe.br/'

    logging.basicConfig(
    filename = f'{self.instrument}_test.log',
    format='%(asctime)s,%(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO
    )

  def listFiles(self, instrument, url, ext_len=0, ext=''):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    if instrument == 'callisto':
      return [url + node.get('href') for node in soup.find_all('a') if node.get('href').startswith(ext, 0, ext_len)]
    elif instrument == 'imager':
      return [url + node.get('href') for node in soup.find_all('a') if node.get('href').startswith(ext, 0, ext_len)]
    if instrument == 'ionosonde':
      return [url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]
    if instrument == 'magnetometer':
      return [url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

  def checkURL(self, url):
      try:
        urllib.request.urlretrieve(url)
      except urllib.error.HTTPError as err:
        message = 'No data from this date or invalid input stn/date'
        logging.info(f'{err} - {message}: "{url}"')

    #def returnRangeOfDates(self, start_date, end_date):
  def returnRangeOfDates(self):  
      try:
        range_date = pd.date_range(start=self.start_date, end=self.end_date).strftime('%Y-%m-%d')
        #full_uri = range_date.strftime('%Y-%m-%d')
        return range_date
      except:
        logging.info(f'Invalid date/range of dates!\n\nYour entry dates:\n{self.start_date}\n{self.end_date}')

  def getCallisto(self):
    logging.info(self.checkURL(self.base_url + self.instrument))
    logging.info(self.returnRangeOfDates())
    #info = f'{base_url}{self.instrument}/ {self.start_date} {self.end_date}'
    #if self.instrument == 'callisto':

download = EmbraceData('callisto', '2022-01-01', '2022-01-03')
download.getCallisto()
#ist = EmbraceData('callisto', '2022-01-01', '2022-01-10')
#ist.getCallisto()
