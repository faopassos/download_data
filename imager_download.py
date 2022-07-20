#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import wget
import os


stn = 'SMS'
year = '2022'
month = '03'
day = '15'
uri = 'https://embracedata.inpe.br/imager/'
uri_dir = stn + '/' + year + '/' + stn + '_' + year + '_' + month + day
url = uri + uri_dir + '/'
exts = ['OH-DARK', 'O6-DARK']

def makeDir(path):
    base_dir = os.getcwd()
    os.makedirs(base_dir + '/data/' + path, exist_ok=True)


def listFD(url, ext=''):
  page = requests.get(url).text
  soup = BeautifulSoup(page, 'html.parser')
  return [url + node.get('href') for node in soup.find_all('a') if node.get('href').startswith(ext, 0, 7)]


data_dir = 'imager' + '/' + uri_dir
makeDir(data_dir)

for ext in exts:
  for file in listFD(url, ext):
    print(file)
    wget.download(file, 'data/' + data_dir)