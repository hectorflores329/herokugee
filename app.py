from flask import Flask
import folium
import folium.plugins as plugins
import numpy as np
import pandas as pd
import requests
import geopandas
import branca
from datetime import datetime, timedelta
from folium.plugins import FloatImage
from folium.plugins import Draw
from folium.plugins import MiniMap
from folium.features import GeoJsonPopup, GeoJsonTooltip

app = Flask(__name__)

@app.route('/')
def mapa():

    response = requests.get(
        "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/us-states.json"
    )
    data = response.json()
    states = geopandas.GeoDataFrame.from_features(data, crs="EPSG:4326")

    return states.to_html(header="true", table_id="table")

    # m = folium.Map(location=[35.3, -97.6], zoom_start=4)

    # return m._repr_html_()

if __name__ == '__main__':
    app.run()
