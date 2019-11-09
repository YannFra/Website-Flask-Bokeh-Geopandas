# -*- coding: utf-8 -*-



"""https://data.sfgov.org/Transportation/SFMTA-Bikeway-Network/ygmz-vaxd"""

# In[1]:
"""Download the dataset form the website"""
import os

from urllib.request import urlretrieve

url_db="https://data.sfgov.org/api/geospatial/ygmz-vaxd?method=export&format=Shapefile"
 
data_dir="data"
zip_name="bikeway_network.zip"
zip_path=data_dir+"/"+zip_name

try:os.mkdir(data_dir)
except:pass
                 
if not os.path.exists(zip_path):
    urlretrieve(url_db,zip_path)
    print("Zip file containing the shapefile downloaded")
else:
    print("Zip file containing the shapefile already there")
    
    
import zipfile
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(data_dir)