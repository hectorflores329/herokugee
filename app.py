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
        "https://ide.dataintelligence-group.com/geoserver/glaciares/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=glaciares%3AR14_Subcuencas_Glaciares&maxFeatures=50&outputFormat=application%2Fjson"
    )
    data = response.json()
    states = geopandas.GeoDataFrame.from_features(data, crs="EPSG:4326")

    # return states.to_html(header="true", table_id="table")

    m = folium.Map(location=[-33.48621795345005, -70.66557950912359], zoom_start=4)
    popup = GeoJsonPopup(
        fields=["NOM_CUENCA"],
        aliases=["COD_CUENCA"],
        localize=True,
        labels=True,
        style="background-color: yellow;",
    )

    tooltip = GeoJsonTooltip(
        fields=["NOM_CUENCA"],
        aliases=["COD_CUENCA:"],
        localize=True,
        sticky=False,
        labels=True,
        style="""
            background-color: #F0EFEF;
            border: 2px solid black;
            border-radius: 3px;
            box-shadow: 3px;
        """,
        max_width=800,
    )

    g = folium.GeoJson(
        data,
        tooltip=tooltip,
        popup=popup
    ).add_to(m)

    folium.LayerControl().add_to(m)

    return m._repr_html_()

@app.route('/tabla')
def tabla():
    response = requests.get(
        "https://ide.dataintelligence-group.com/geoserver/glaciares/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=glaciares%3AR14_Subcuencas_Glaciares&maxFeatures=50&outputFormat=application%2Fjson"
    )
    data = response.json()
    states = geopandas.GeoDataFrame.from_features(data, crs="EPSG:4326")
    
    return states.to_html(header="true", table_id="table")

if __name__ == '__main__':
    app.run()
