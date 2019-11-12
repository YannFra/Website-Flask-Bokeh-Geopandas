# How to plot an interactive plot in a website. All in Python.

You have a dataset. How do you plot this dataset into a website? Well guess what, here again Python can do all of that. From opening the dataset to creating a webpage including the interactive plot you did, there is nothing Python cannot do! 

This tutorial/example will go through all the steps required to go from the dataset to inserting your dynamic plot in a webpage. We will be plotting the bikeways in San Francisco over the city’s streets. The questions this example answers are:
+	How do you open and plot a geospatial database ? We will use GeoPandas to open a shapefile db (.shp).
+	How do you make this plot interact with the user ? We will use Bokeh to create the interactive plot.
+	How do you create a webpage including this plot ? We will use Flask to do so. 

A lot of tutorials show how to do each of these parts independently. The goal of this tutorial is to include all of them into one example on the Bike Lanes network in San Francisco. The Python code used can be found in this [GitHub](https://github.com/YannFra/Website-Flask-Bokeh-Geopandas) and the explanations in this [tutorial](https://yannfra.github.io/Creating-Website-Flask-Bokeh-GeoPandas/). Please contact me if you encounter any issue. 

Python libraries used in this tutorial: [Bokeh](https://docs.bokeh.org/en/latest/),[Flask](https://www.fullstackpython.com/flask.html), and [GeoPandas](http://geopandas.org)

Our example will be on the bike network in San Francisco. Where are the bike lanes in San Francisco ? Is there enough of them to commute in bike ? We will create a plot that superimposes the bike lanes network to the street network in San Francisco. Then we will allow the user to zoom this plot and to hide/show the desired networks. 

This work was possible thanks to :
+ [DataSF](https://datasf.org) that has a lot of Open Access datasets. We used the one they give on [bike lanes in San Francisco](https://data.sfgov.org/Transportation/SFMTA-Bikeway-Network/ygmz-vaxd).
+ [Data.gov] that also has a lot of open Access datasets. We used the one they give about the [streets in San Francisco](https://catalog.data.gov/dataset/tiger-line-shapefile-2017-county-san-francisco-county-ca-all-roads-county-based-shapefile)
