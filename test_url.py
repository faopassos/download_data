#!/usr/bin/python3

url = ['https://embracedata.inpe.br/callisto/CXP/2022/02/INPE_20220201_194457_59.fit',
      'https://embracedata.inpe.br/callisto/CXP/2022/02/INPE_20220201_194457_59.fit',
      'https://embracedata.inpe.br/callisto/CXP/2022/02/INPE_20220201_194457_59.fit']


for u in url:
    res = u.rsplit('/', 1)[1]
    print(res)
