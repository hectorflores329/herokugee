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
        "https://raw.githubusercontent.com/pri-data/50-states/master/data/income-counties-states-national.csv",
        dtype={"fips": str},
    )
    income["income-2015"] = pd.to_numeric(income["income-2015"], errors="coerce")

    response = requests.get(
        "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/us-states.json"
    )
    data = response.json()
    states = geopandas.GeoDataFrame.from_features(data, crs="EPSG:4326")

    response = requests.get(
        "https://gist.githubusercontent.com/tvpmb/4734703/raw/"
        "b54d03154c339ed3047c66fefcece4727dfc931a/US%2520State%2520List"
    )
    
    colormap = branca.colormap.LinearColormap(
        vmin=income["change"].quantile(0.0),
        vmax=income["change"].quantile(1),
        colors=["red", "orange", "lightblue", "green", "darkgreen"],
        caption="State Level Median County Household Income (%)",
    )

    m = folium.Map(location=[35.3, -97.6], zoom_start=4)

    popup = GeoJsonPopup(
        fields=["name", "change"],
        aliases=["State", "% Change"],
        localize=True,
        labels=True,
        style="background-color: yellow;",
    )

    tooltip = GeoJsonTooltip(
        fields=["name", "medianincome", "change"],
        aliases=["State:", "2015 Median Income(USD):", "Median % Change:"],
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
        income,
        style_function=lambda x: {
            "fillColor": colormap(x["properties"]["change"])
            if x["properties"]["change"] is not None
            else "transparent",
            "color": "black",
            "fillOpacity": 0.4,
        },
        tooltip=tooltip,
        popup=popup,
    ).add_to(m)

    colormap.add_to(m)

    # folium.LayerControl().add_to(m)


    return m._repr_html_()
    # return HeatMapWithTime(lat_long_list2,radius=5,auto_play=True,position='bottomright').add_to(map)

if __name__ == '__main__':
    app.run()
