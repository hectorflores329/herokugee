import ee
import geemap

from flask import Flask
import folium
from folium import plugins

app = Flask(__name__)

@app.route('/')
def mapa():

    ee.Authenticate()
    ee.Initialize()
    
    # Print the elevation of Mount Everest.
    dem = ee.Image('USGS/SRTMGL1_003')
    xy = ee.Geometry.Point([86.9250, 27.9881])
    elev = dem.sample(xy, 30).first().get('elevation').getInfo()
    print('Mount Everest elevation (m):', elev)

    m = folium.Map(location=[-33.48621795345005, -70.66557950912359], zoom_start=4)

    return m._repr_html_()
    # return HeatMapWithTime(lat_long_list2,radius=5,auto_play=True,position='bottomright').add_to(map)

if __name__ == '__main__':
    app.run()
