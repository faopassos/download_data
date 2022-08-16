import embracedata_download


get_data = embracedata_download.Embrace_Data()

#YYYY-MM-DD
CALLISTO = { 
  'start_date': '2022-01-31',
  'end_date': '2022-01-31'
}
get_data.Callisto(CALLISTO['start_date'], CALLISTO['end_date'])


#YYYY-MM-DD
# all available stations: 'BJL', 'BV', 'CA', 'CP', 'SMS'
# all available filters: 'O6', 'OH', 'O6-DARK', 'OH-DARK'
IMAGER = {
  'start_date': '2022-01-01',
  'end_date': '2022-01-02',
  'stations': ['BJL', 'CA', 'CP'],
  'filters': ['O6-DARK', 'OH-DARK']
}
get_data.Imager(IMAGER['start_date'], IMAGER['end_date'], IMAGER['stations'], IMAGER['filters'])


#YYYY-DOY
# all available stations: 'BLJ03', 'BVJ03', 'CAJ2M', 'CGK21', 'FZA0M', 'SAA0K', 'SMK29'
# all available extensions: '.RSF', '.SAO', '.PNG', '.DFT', '.DVL', '.SKY' 'SAO.XML'
IONOSONDE = {
  'start_date': '2020-036',
  'end_date': '2020-036',
  'stations': ['BLJ03', 'SAA0K'],
  'extensions': ['.SAO', '.RSF']
}
get_data.Ionosonde(IONOSONDE['start_date'], IONOSONDE['end_date'], IONOSONDE['stations'], IONOSONDE['extensions'])


#YYYY-DOY
# all available stations: 'ALF', 'ARA', 'CBA', 'CHI', 'CXP', 'EUS', 'JAT', 'MAN','MED',
#                         'PAL', 'PVE', 'RGA', 'SJC', 'SLZ', 'SMS', 'STM', 'TCM', 'VSS'
MAGNETOMETER = {
  'start_date': '2022-01-01',
  'end_date': '2022-01-10',
  'stations': ['ALF', 'ARA', 'CBA']
}
get_data.Magnetometer(MAGNETOMETER['start_date'], MAGNETOMETER['end_date'], MAGNETOMETER['stations'])
