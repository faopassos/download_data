#!/usr/bin/python3
from email.mime import base


class downloadData:
  def __init__(self, instrument, start_date, end_date):
    self.instrument = instrument
    self.start_date = start_date
    self.end_date = end_date

  def showInfos(self):
    base_url = 'https://embracedata.inpe.br/'
    info = f'{base_url}{self.instrument}/\n{self.start_date}\n{self.end_date}'
    if self.instrument == 'callisto':
      print(info)
    elif self.instrument == 'imager':
      print(info)
    elif self.instrument == 'ionosonde':
      print(info)
    elif self.instrument == 'magnetometer':
      print(info)
    else:
      print(f'"{self.instrument}" is not valid')


ist = downloadData('magnetometer', '2022-01-01', '2022-01-10')
ist.showInfos()
