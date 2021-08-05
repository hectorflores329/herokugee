from flask import Flask
import pandas as pd
import folium

app = Flask(__name__)

@app.route('/')
def temp():

    url = (
        "https://raw.githubusercontent.com/hectorflores329/herokugee/main"
    )
    puntos = f"{url}/Región Metropolitana de Santiago, TEMP.xlsx"
    df = pd.read_excel(puntos)

    _map = folium.Map(
        location=[-33.467890412071654, -70.66557950912359],
        zoom_start=4,
        )

    return _map._repr_html_()

if __name__ == '__main__':
    app.run()