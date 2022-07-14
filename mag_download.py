from bs4 import BeautifulSoup
import requests
import wget
import os

url = 'https://embracedata.inpe.br/magnetometer/CXP/2022/'
# by month
ext = ['jun.22m', 'jul.22m']

print(os.getcwd)
os.makedirs(os.getcwd() + '/data/magnetometer/')

def listFD(url, ext=''):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    return [url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]


for extn in ext:
  for file in listFD(url, extn):
    print(file)
    wget.download(file, './data/magnetometer/')

