#!/usr/bin/env python

import pandas as pd
import numpy as np

url = 'https://data.cityofnewyork.us/resource/qiz3-axqb.json?$limit=50&\
$where=date%20between%20%272017-09-30T00:00:00%27%20and%20%272018-09-30T00:00:00%27'
collisions = pd.read_json(url)

updated_long = collisions.iloc[:,7:8]
updated_lat  = collisions.iloc[:,5:6]
lat = updated_lat.values.tolist()
lng = updated_long.values.tolist()

with open('lat.txt', 'w') as f:
    for item in lat:
        f.write("%s\n" % item[0])

with open('long.txt', 'w') as f:
    for item in lng:
        f.write("%s\n" % item[0])
		
