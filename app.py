from flask import Flask
import folium
import folium.plugins as plugins
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from folium.plugins import FloatImage
from folium.plugins import Draw
from folium.plugins import MiniMap
import geopandas

app = Flask(__name__)

@app.route('/')
def mapa():

    m = folium.Map(
        location=[-33.48621795345005, -70.66557950912359],
        min_zoom = 8,
        max_zoom = 100,
        control_scale=True
        # tiles = "openstreetmap"
    )

    states = geopandas.read_file(
        "https://rawcdn.githack.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json",
        driver="GeoJSON",
    )

    cities = geopandas.read_file(
        "https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_50m_populated_places_simple.geojson",
        driver="GeoJSON",
    )

    return m._repr_html_()
    # return HeatMapWithTime(lat_long_list2,radius=5,auto_play=True,position='bottomright').add_to(map)

if __name__ == '__main__':
    app.run()
