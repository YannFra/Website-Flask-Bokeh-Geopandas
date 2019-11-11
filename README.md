# How to plot an interactive plot in a website. All in Python.

You have a shapefile dataset. How do you plot this dataset into a website? Well guess what, here again Python can do all of that. From opening the dataset to creating a webpage including the interactive plot you did, there is nothing Python cannot do! 

This tutorial/example will go through all the steps required to go from the dataset to inserting your dynamic plot in a webpage. We will be plotting the bikeways in San Francisco over the city’s streets. The questions this example answers are:

•	How do you open and plot a geospatial database? We will use GeoPandas to open a shapefile db (.shp).

•	How do you make this plot interact with the user? We will use Bokeh to create the interactive plot.

•	How do you create a webpage including this plot? We will use Flask to do so. 

A lot of tutorials show how to do each of these parts independently. The goal of this tutorial is to include all of them into one example. The Python code used will be displayed in the tutorial. It can also be found in this GitHub. Please contact me if you have any issue. 


Example of a simple website created with the Flask Library for a dynamic plot made with the Bokeh Library to plot a Geopandas db

The dataset for the bike lanes was obtained thanks to DataSF giving acces for free to a lot of datasets and to SFMTA that uploaded it.
https://data.sfgov.org/Transportation/SFMTA-Bikeway-Network/ygmz-vaxd

The dataset to hve all the streets in San Francsisco
https://catalog.data.gov/dataset/tiger-line-shapefile-2017-county-san-francisco-county-ca-all-roads-county-based-shapefile
