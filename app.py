from flask import Flask
import folium
import folium.plugins as plugins
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from folium.plugins import FloatImage
from folium.plugins import Draw
from folium.plugins import MiniMap

app = Flask(__name__)

@app.route('/')
def mapa():

    m = folium.Map(
        location=[-33.48621795345005, -70.66557950912359],
        zoom_start=5,
        min_zoom = 8,
        max_zoom = 30,
        control_scale=True
        # tiles = "openstreetmap"
    )

    w = folium.WmsTileLayer(url = 'https://ide.dataintelligence-group.com/geoserver/chile/wms',

        layers = 'chile:Regiones',
        fmt ='image/png',
        transparent = True,
        name = "Regiones",
        control = True,
        attr = "Mapa de Chile"
    )

    w.add_to(m)

    folium.TileLayer('openstreetmap').add_to(m)
    folium.TileLayer('cartodbpositron').add_to(m)
    folium.TileLayer('cartodbdark_matter').add_to(m)
    folium.LayerControl().add_to(m)


    return m._repr_html_()
    # return HeatMapWithTime(lat_long_list2,radius=5,auto_play=True,position='bottomright').add_to(map)

if __name__ == '__main__':
    app.run()
