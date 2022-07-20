#!/usr/bin/python3
import urllib.request
import urllib.error

def checkURL(url, message):
    try:
        urllib.request.urlretrieve(url)
    except urllib.error.HTTPError as err:
        return f'{err} - {message}'


url = 'https://embracedata.inpe.br/imager/CP/2021/CP_2021_011800/'
error_message = 'No data from this date or invalid date.'
print(checkURL(url, error_message))
