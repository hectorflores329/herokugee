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
    income = pd.read_csv(
        "https://ide.dataintelligence-group.com/geoserver/glaciares/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=glaciares%3AR14_Subcuencas_Glaciares&maxFeatures=50&outputFormat=application%2Fjson",
        dtype={"fips": str},
    )
    
    print(income)

    m = folium.Map(location=[35.3, -97.6], zoom_start=4)

    return m._repr_html_()
    # return HeatMapWithTime(lat_long_list2,radius=5,auto_play=True,position='bottomright').add_to(map)

if __name__ == '__main__':
    app.run()
