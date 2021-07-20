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

    folium.raster_layers.TileLayer(
        tiles='http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
        attr='google',
        name='google maps',
        max_zoom=20,
        subdomains=['mt0', 'mt1', 'mt2', 'mt3'],
        overlay=False,
        control=True,
    ).add_to(m)

    folium.raster_layers.WmsTileLayer(
        url='http://mesonet.agron.iastate.edu/cgi-bin/wms/nexrad/n0r.cgi',
        name='test',
        fmt='image/png',
        layers='nexrad-n0r-900913',
        attr=u'Weather data © 2012 IEM Nexrad',
        transparent=True,
        overlay=True,
        control=True,
        interactive=False,
    ).add_to(m)

    folium.features.RegularPolygonMarker(-33.48621795345005, -70.66557950912359, color='black', opacity=1, weight=2, fill_color='blue', fill_opacity=1, number_of_sides=4, rotation=0, radius=15, popup=None)

    w1.add_to(m)

    # folium.LatLngPopup().add_to(m)

    folium.LayerControl().add_to(m)


    return m._repr_html_()
    # return HeatMapWithTime(lat_long_list2,radius=5,auto_play=True,position='bottomright').add_to(map)

if __name__ == '__main__':
    app.run()
