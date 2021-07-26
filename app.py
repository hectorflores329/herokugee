import ee
import geemap

from flask import Flask
import folium

app = Flask(__name__)

@app.route('/')
def mapa():

    ee.Initialize()
    sentinel1 = ee.ImageCollection('COPERNICUS/S1_GRD').filterBounds(ee.Geometry.Point(-122.37383, 37.6193))

    m = folium.Map(location=[-33.48621795345005, -70.66557950912359], zoom_start=4)

    return m._repr_html_()
    # return HeatMapWithTime(lat_long_list2,radius=5,auto_play=True,position='bottomright').add_to(map)

if __name__ == '__main__':
    app.run()
