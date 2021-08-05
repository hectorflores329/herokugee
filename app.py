from flask import Flask
import pandas as pd
import folium

app = Flask(__name__)

@app.route('/')
def temp():

    _map = folium.Map(
        location=[-33.467890412071654, -70.66557950912359],
        zoom_start=4,
        )

    return _map._repr_html_()

if __name__ == '__main__':
    app.run()