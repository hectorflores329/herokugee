from flask import Flask
import folium
import folium.plugins as plugins
import numpy as np
import pandas as pd
import ee
from datetime import datetime, timedelta
from folium.plugins import FloatImage
from folium.plugins import Draw
from folium.plugins import MiniMap
import folium
from folium import plugins

app = Flask(__name__)

@app.route('/')
def mapa():

    
    # Create a folium map object.
    m = folium.Map(location=[40.33, -99.42], zoom_start=4)
    
    return m._repr_html_()
    # return HeatMapWithTime(lat_long_list2,radius=5,auto_play=True,position='bottomright').add_to(map)

if __name__ == '__main__':
    app.run()
