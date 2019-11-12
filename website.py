# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    
    import geopandas as gpd
    
    db_bike_path="data/geo_export_0ff3043a-1833-476b-afe0-779dfa091ebd.shp"
    db_bike=gpd.read_file(db_bike_path)
    
    db_roads_path="data/tl_2017_06075_roads.shp"
    db_roads=gpd.read_file(db_roads_path)
    
    
    #Libraries for Dynamic Vizualisation
    from bokeh.plotting import figure
    from bokeh.models import GeoJSONDataSource
    from bokeh.embed import components
    from bokeh.resources import INLINE
    from flask import render_template

    SF = figure(aspect_scale=1, match_aspect=True)
    
    db_roads_json=GeoJSONDataSource(geojson = db_roads.to_json())
    SF.multi_line('xs', 'ys', source=db_roads_json,
        color="gray", line_width=0.5,legend="All streets")
    
    db_bike_json=GeoJSONDataSource(geojson = db_bike.to_json())
    SF.multi_line('xs', 'ys', source=db_bike_json,
        color="red", line_width=1.5,legend="Bike Lanes")
    
    SF.legend.click_policy="hide"
    
    script_plot,div_plot=components(SF ,INLINE)
    
    return render_template('plot.html',
                       script=script_plot,
                       div=div_plot,
                       js_resources=INLINE.render_js(),
                       css_resources=INLINE.render_css())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)