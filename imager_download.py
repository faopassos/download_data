#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import wget
import os
import urllib.request
import urllib.error


stn = 'BV'
year = '2015'
month = '03'
day = '15'
filters = ['OH-DARK', 'O6-DARK', 'O5-DARK']

uri = 'https://embracedata.inpe.br/imager/'
uri_dir = stn + '/' + year + '/' + stn + '_' + year + '_' + month + day
url = uri + uri_dir + '/'

def checkURL(url, message):
  try:
    urllib.request.urlretrieve(url)
  except urllib.error.HTTPError as err:
      print(f'{err} - {message}: {url}')
      exit()


def makeDir(path):
  base_dir = os.getcwd()
  os.makedirs(base_dir + '/data/' + path, exist_ok=True)


def listFD(url, ft_len, ft=''):
  page = requests.get(url).text
  soup = BeautifulSoup(page, 'html.parser')
  return [url + node.get('href') for node in soup.find_all('a') if node.get('href').startswith(ft, 0, ft_len)]


if __name__ == '__main__':
  error_message = 'No data from this date or invalid date/stn'
  checkURL(url, error_message)

  data_dir = 'imager' + '/' + uri_dir
  makeDir(data_dir)

  for ft in filters:
    if listFD(url, len(ft), ft) == []:
      print(f'\nNo file match with filter "{ft}"')
    else:
      for file in listFD(url, len(ft), ft):
        print(f'\n{file}')
        wget.download(file, 'data/' + data_dir)
