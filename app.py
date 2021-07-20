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
        min_zoom = 8,
        max_zoom = 100,
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

    w1 = folium.WmsTileLayer(url = 'https://ide.dataintelligence-group.com/geoserver/glaciares/wms',

        layers = 'glaciares:porcR10_02_glaciar_zona_monitoreada',
        fmt ='image/png',
        transparent = True,
        name = "Glaciares",
        control = True,
        attr = "Glaciares"
    )

    w1.add_to(m)

    folium.LatLngPopup().add_to(m)

    folium.LayerControl().add_to(m)


    return m._repr_html_()
    # return HeatMapWithTime(lat_long_list2,radius=5,auto_play=True,position='bottomright').add_to(map)

if __name__ == '__main__':
    app.run()
