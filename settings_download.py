CALLISTO = {
  #YYYY-MM-DD
  'start_date': '2022-01-01',
  'end_date': '2022-01-02'
}

#YYYY-MM-DD
# all available stations: 'BJL', 'BV', 'CA', 'CP', 'SMS'
# all available filters: 'O6', 'OH', 'O6-DARK', 'OH-DARK'
IMAGER = {
  'start_date': '2022-01-01',
  'end_date': '2022-01-02',
  'stations': ['BJL', 'CA', 'CP'],
  'filters': ['O6-DARK', 'OH-DARK']
}

#YYYY-DOY
# all available stations: 'BLJ03', 'BVJ03', 'CAJ2M', 'CGK21', 'FZA0M', 'SAA0K', 'SMK29'
# all available extensions: '.RSF', '.SAO', '.PNG', '.DFT', '.DVL', '.SKY' 'SAO.XML'
IONOSONDE = {
  'start_date': '2022-001',
  'end_date': '2022-002',
  'stations': ['BLJ03', 'SAA0K'],
  'extensions': ['.SAO', '.RSF']
}

#YYYY-DOY
# all available stations: 'ALF', 'ARA', 'CBA', 'CHI', 'CXP', 'EUS', 'JAT', 'MAN','MED',
#                         'PAL', 'PVE', 'RGA', 'SJC', 'SLZ', 'SMS', 'STM', 'TCM', 'VSS'
MAGNETOMETER = {
  'start_date': '2022-01-01',
  'end_date': '2022-01-02',
  'stations': ['ALF', 'ARA', 'CBA']
}
