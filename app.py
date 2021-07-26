import subprocess

try:
    import geemap
except ImportError:
    print('Installing geemap ...')
    subprocess.check_call(["python", '-m', 'pip', 'install', 'geemap'])


import ee
import geemap

from flask import Flask
import folium
from folium import plugins

app = Flask(__name__)

@app.route('/')
def mapa():

    Map = geemap.Map(center=[40,-100], zoom=4)
    
    m = folium.Map(location=[-33.48621795345005, -70.66557950912359], zoom_start=4)

    return m._repr_html_()
    # return HeatMapWithTime(lat_long_list2,radius=5,auto_play=True,position='bottomright').add_to(map)

if __name__ == '__main__':
    app.run()
