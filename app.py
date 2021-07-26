import ee
import geemap

from flask import Flask
import folium

app = Flask(__name__)

@app.route('/')
def mapa():

    m = geemap.Map(center=(40, -100), zoom=4)

    return m._repr_html_()
    # return HeatMapWithTime(lat_long_list2,radius=5,auto_play=True,position='bottomright').add_to(map)

if __name__ == '__main__':
    app.run()
