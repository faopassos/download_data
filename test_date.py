#!/usr/bin/python3

import pandas as pd
#from datetime import datetime


date_range = pd.date_range(start="2020-02-01",end="2020-02-03")

print(date_range)

for day in date_range:
  print(day.strftime("dddSS%Y%m%d"))
