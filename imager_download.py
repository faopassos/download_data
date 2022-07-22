#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import wget
import os
import urllib.request
import urllib.error


stn = 'SMS'
year = '2022'
month = '03'
day = '15'
uri = 'https://embracedata.inpe.br/imager/'
uri_dir = stn + '/' + year + '/' + stn + '_' + year + '_' + month + day
url = uri + uri_dir + '/'
exts = ['OH-DARK', 'O6-DARK', 'O5-DARK']

def checkURL(url, message):
    try:
        urllib.request.urlretrieve(url)
    except urllib.error.HTTPError as err:
        print(f'{err} - {message}: {url}')
        exit()


error_message = 'No data from this date or invalid date/stn'
checkURL(url, error_message)

def makeDir(path):
    base_dir = os.getcwd()
    os.makedirs(base_dir + '/data/' + path, exist_ok=True)


def listFD(url, ext_len, ext=''):
  page = requests.get(url).text
  soup = BeautifulSoup(page, 'html.parser')
  return [url + node.get('href') for node in soup.find_all('a') if node.get('href').startswith(ext, 0, ext_len)]


data_dir = 'imager' + '/' + uri_dir
makeDir(data_dir)

for ext in exts:
  for file in listFD(url, len(ext), ext):
    print(file)
    wget.download(file, 'data/' + data_dir)
