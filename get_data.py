import embracedata_download


CALLISTO = { 
  'start_date': '2022-01-15',
  'end_date': '2022-01-31'
}

IMAGER = {
  'start_date': '2022-01-29',
  'end_date': '2022-01-31',
  'stations': ['CA', 'CP'],
  'filters': ['O6-DARK', 'OH-DARK']
}

IONOSONDE = {
  'start_date': '2020-035',
  'end_date': '2020-036',
  'stations': ['BLJ03'],
  'extensions': ['.SAO']
}

LIDAR = {
  'start_date': '2022-07-28',
  'end_date': '2022-07-30',
  'elements': ['Potassium', 'Sodium']
}

MAGNETOMETER = {
  'start_date': '2022-02-03',
  'end_date': '2022-02-05',
  'stations': ['ALF', 'ARA']
}

SCINTILLATION = {
  'start_date': '2021-046',
  'end_date': '2021-047',
  'stations': ['imp', 'ios']
}

def download_Files():
  get_data = embracedata_download.Embrace_Data()
  #get_data.Callisto(**CALLISTO)
  #get_data.Imager(**IMAGER)
  #get_data.Ionosonde(**IONOSONDE)
  #get_data.Lidar(**LIDAR)
  #get_data.Magnetometer(**MAGNETOMETER)
  get_data.Scintillation(**SCINTILLATION)

if __name__ == '__main__':
  download_Files()
