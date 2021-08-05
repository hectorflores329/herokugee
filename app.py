from flask import Flask
import pandas as pd
import folium

app = Flask(__name__)

@app.route('/')
def temp():

    puntos = "https://github.com/hectorflores329/herokugee/raw/main/Regi%C3%B3n%20Metropolitana%20de%20Santiago%2C%20TEMP.xlsx"
    df = pd.read_excel(puntos)

    _map = folium.Map(
        location=[-33.467890412071654, -70.66557950912359],
        zoom_start=4,
        )

    return _map._repr_html_()

if __name__ == '__main__':
    app.run()