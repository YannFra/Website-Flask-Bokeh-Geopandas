# -*- coding: utf-8 -*-
# In[9]:

import geopandas as gpd

db_bike_path="data/geo_export_0ff3043a-1833-476b-afe0-779dfa091ebd.shp"
db_bike=gpd.read_file(db_bike_path)


db_roads_path="data/tl_2017_06075_roads.shp"
db_roads=gpd.read_file(db_roads_path)


# In[9]:
from bokeh.models import GeoJSONDataSource
db_roads_json=GeoJSONDataSource(geojson = db_roads.to_json())
db_bike_json=GeoJSONDataSource(geojson = db_bike.to_json())


# In[9]:
#Libraries for Dynamic Vizualisation
from bokeh.plotting import figure
from bokeh.io import output_file,show
from bokeh.layouts import  row, column, layout
from bokeh.models.widgets import CheckboxGroup
from bokeh.models import CustomJS

SF = figure(aspect_scale=1, match_aspect=True,sizing_mode='scale_height')
SF.xaxis.axis_label='Longitude'
SF.yaxis.axis_label='Latitude'


multi_line_all=SF.multi_line('xs', 'ys', source=db_roads_json,
    color="gray", line_width=0.5,legend="All streets")

multi_line_bike=SF.multi_line('xs', 'ys', source=db_bike_json,
    color="red", line_width=1.5,legend="Bike Lanes")

checkbox_choices = CheckboxGroup(labels=["All streets", "Bike Lanes"], 
    active=[i for i in range(2)])

SF.legend.location = "top_left"
SF.legend.click_policy="hide"

#output_file("foo.html")


updatingRequiredParameters=dict(curves=[multi_line_all,multi_line_bike],
    check=checkbox_choices)

updatingJS="""
    var coefs=check.active;
    
    for (var i = 0; i<= coefs.length; i++){
        console.log(coefs.includes(i))
        if (coefs.includes(i)){
            curves[i].visible=true;
        }
        else{
            curves[i].visible=false;
        }
    }    
"""
checkbox_choices.callback=CustomJS(args=updatingRequiredParameters,code=updatingJS)


layout=row(SF,checkbox_choices)


show(layout)






















