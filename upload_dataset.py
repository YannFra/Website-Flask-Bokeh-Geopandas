# -*- coding: utf-8 -*-

"""Download the dataset form DataSF. The url used for the download might no 
longer be the smae as the one I was given when I did this example.
I have put the datasets in the Github anyway. This ode is just for your curiosity"""

import os
import zipfile
from urllib.request import urlretrieve

url_bike_db="https://data.sfgov.org/api/geospatial/ygmz-vaxd?method=export&format=Shapefile"
url_street_db="https://catalog.data.gov/dataset/tiger-line-shapefile-2017-county-san-francisco-county-ca-all-roads-county-based-shapefile"

#create the folder where we will save our dataset and our plots
data_dir="data"
try:os.mkdir(data_dir)
except:pass

try:os.mkdir("templates")
except:pass


#Downlaod the bike zip file available on the website if not already in `data`
bike_zip_name="bikeway_network.zip"
bike_zip_path=data_dir+"/"+bike_zip_name
                 
if not os.path.exists(bike_zip_path):
    
    print("Downloading Bike Zip file")
    urlretrieve(url_bike_db,bike_zip_path)
    print("Download finished.")
          
    print("Starting unzipping")
    with zipfile.ZipFile(bike_zip_path, 'r') as zip_ref:
        zip_ref.extractall(data_dir)
    print("Bike Zip file unzipped")
    
else:
    print("Bike Network Db file already downloaded")
    
    
#Downlaod the streets zip file available on the website if not already in `data`
street_zip_name="streets_SF.zip"
street_zip_path=data_dir+"/"+street_zip_name
                 
if not os.path.exists(street_zip_path):
    
    print("Downloading Street SF Zip file")
    urlretrieve(url_street_db,street_zip_path)
    print("Download finished.")
          
    print("Starting unzipping")
    with zipfile.ZipFile(bike_zip_path, 'r') as zip_ref:
        zip_ref.extractall(data_dir)
    print("Street SF Zip unzipped")
    
else:
    print("Streets SF Db file already downloaded") 