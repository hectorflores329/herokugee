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

    states = geopandas.read_file(
        "https://rawcdn.githack.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json",
        driver="GeoJSON",
    )

    cities = geopandas.read_file(
        "https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_50m_populated_places_simple.geojson",
        driver="GeoJSON",
    )

    states_sorted = states.sort_values(by="density", ascending=False)
    states_sorted.head(5).append(states_sorted.tail(5))[["name", "density"]]

    def rd2(x):
        return round(x, 2)

    minimum, maximum = states["density"].quantile([0.05, 0.95]).apply(rd2)
    mean = round(states["density"].mean(), 2)

    us_cities = geopandas.sjoin(cities, states, how="inner", op="within")
    pop_ranked_cities = us_cities.sort_values(by="pop_max", ascending=False)[
        ["nameascii", "pop_max", "geometry"]
    ].iloc[:20]

    m = folium.Map(location=[38, -97], zoom_start=4)


    def style_function(x):
        return {
            "fillColor": colormap(x["properties"]["density"]),
            "color": "black",
            "weight": 2,
            "fillOpacity": 0.5,
        }


    stategeo = folium.GeoJson(
        states,
        name="US States",
        style_function=style_function,
        tooltip=folium.GeoJsonTooltip(
            fields=["name", "density"], aliases=["State", "Density"], localize=True
        ),
    ).add_to(m)

    citygeo = folium.GeoJson(
        pop_ranked_cities,
        name="US Cities",
        tooltip=folium.GeoJsonTooltip(
            fields=["nameascii", "pop_max"], aliases=["", "Population Max"], localize=True
        ),
    ).add_to(m)


    folium.LayerControl().add_to(m)

    return m._repr_html_()
    # return HeatMapWithTime(lat_long_list2,radius=5,auto_play=True,position='bottomright').add_to(map)

if __name__ == '__main__':
    app.run()
