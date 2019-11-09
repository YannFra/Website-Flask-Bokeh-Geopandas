# -*- coding: utf-8 -*-

"""Download the dataset form DataSF. The url used for the download might no 
longer be the smae as the one I was given when I did this example.
I have put the datasets in the Github anyway. This ode is just for your curiosity"""

import os
import zipfile
from urllib.request import urlretrieve

url_db="https://data.sfgov.org/api/geospatial/ygmz-vaxd?method=export&format=Shapefile"

#create the folder where we will save our dataset 
data_dir="data"
try:os.mkdir(data_dir)
except:pass


#Downlaod the zip file available on the website if not already in `data`
zip_name="bikeway_network.zip"
zip_path=data_dir+"/"+zip_name
                 
if not os.path.exists(zip_path):
    urlretrieve(url_db,zip_path)
    print("Zip file containing the shapefile downloaded")
else:
    print("Zip file containing the shapefile already there")
    
    
#Unzip the zip file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(data_dir)