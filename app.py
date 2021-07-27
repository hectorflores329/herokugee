import folium
from flask import Flask
import ee
import geehydro

app = Flask(__name__)

@app.route('/')
def mapa():
    
    # Get a composite of all Sentinal 2 images within a date range that include my point of interest.
    poi = ee.Geometry.Point([-82.4572, 27.9506])

    m = folium.Map(location=[-33.48621795345005, -70.66557950912359], zoom_start=4)
    return m._repr_html_()


if __name__ == '__main__':
    app.run()
