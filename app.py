from flask import Flask
import pandas as pd
import folium

app = Flask(__name__)

@app.route('/')
def temp():

    
    _map = folium.Map(
        location=[40.712776, -74.005974],
        zoom_start=5,
        width = 850,
        height = 650,
        min_zoom = 8,
        max_zoom = 14
        )

    return _map._repr_html_()

if __name__ == '__main__':
    app.run()