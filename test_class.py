#!/usr/bin/python3
from bs4 import BeautifulSoup
import pandas as pd
import requests, wget, os, urllib.request, urllib.error, logging


class downloadData:
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

  def checkURL(url):
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

  def showInfos(self):
    logging.info(self.checkURL(self.base_url + self.instrument))
    logging.info(self.returnRangeOfDates())
    #info = f'{base_url}{self.instrument}/ {self.start_date} {self.end_date}'
    #if self.instrument == 'callisto':

ist = downloadData('callisto', '2022-01-01', '2022-01-10')
ist.showInfos()
