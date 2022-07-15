from bs4 import BeautifulSoup
import requests
import wget
import os


url = 'https://embracedata.inpe.br/ionosonde/CAJ2M/2022/014/'
# by month
exts = ['.RSF', '.SAO']

data_dir = os.getcwd() + '/data/ionosonde/'
os.makedirs(data_dir, exist_ok=True)

def listFD(url, ext=''):
  page = requests.get(url).text
  soup = BeautifulSoup(page, 'html.parser')
  return [url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

for ext in exts:
  for file in listFD(url, ext):
    print(file)
    wget.download(file, data_dir)
