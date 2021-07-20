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
    abbrs = pd.read_json(response.text)

    statesmerge = states.merge(abbrs, how="left", left_on="name", right_on="name")
    statesmerge["geometry"] = statesmerge.geometry.simplify(0.05)

    income.groupby(by="state")[["state", "income-2015"]].median().head()

    statesmerge["medianincome"] = statesmerge.merge(
        income.groupby(by="state")[["state", "income-2015"]].median(),
        how="left",
        left_on="alpha-2",
        right_on="state",
    )["income-2015"]
    statesmerge["change"] = statesmerge.merge(
        income.groupby(by="state")[["state", "change"]].median(),
        how="left",
        left_on="alpha-2",
        right_on="state",
    )["change"]

    m = folium.Map(
        location=[-33.48621795345005, -70.66557950912359],
        min_zoom = 8,
        max_zoom = 100,
        control_scale=True
        # tiles = "openstreetmap"
    )

    
    colormap = branca.colormap.LinearColormap(
        vmin=statesmerge["change"].quantile(0.0),
        vmax=statesmerge["change"].quantile(1),
        colors=["red", "orange", "lightblue", "green", "darkgreen"],
        caption="State Level Median County Household Income (%)",
    )

    folium.LayerControl().add_to(m)


    return m._repr_html_()
    # return HeatMapWithTime(lat_long_list2,radius=5,auto_play=True,position='bottomright').add_to(map)

if __name__ == '__main__':
    app.run()
