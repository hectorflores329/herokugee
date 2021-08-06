from flask import Flask
from folium.map import FeatureGroup, Popup
import pandas as pd
import folium
from flask import request

app = Flask(__name__)

@app.route('/')
def temp():

    try:
        comuna = request.args.get("comuna")
        comuna = int(comuna)
    except:
        comuna = 0

    puntos = "https://raw.githubusercontent.com/hectorflores329/herokugee/main/Regi%C3%B3n%20Metropolitana%20de%20Santiago%2C%20TEMP.csv"
    df = pd.read_csv(puntos)

    df = df[df["COMUNA"] == comuna]

    latitude = df["latitude"].tolist()
    longitude = df["longitude"].tolist()
    nomCom = df["NOM_COMUNA"].tolist()

    locations = []

    for lat, lon in zip(latitude, longitude):
        fLat = float(lat)
        fLon = float(lon)
        locations.append((lat, lon, nomCom))

    _map = folium.Map(
        location=[-33.467890412071654, -70.66557950912359],
        zoom_start=10,
    )

    texto = "Este es un texto python"
    
    for coord in locations:
        html="""
        <style>
            h1{
                color:yellow;
            }
        </style>

        <div>
            <div>
                <br>
                <div>
                    <div><p>Este es un párrafo en un div.</p></div>
                    <div><p>Este es un párrafo en un div.</p></div>
                    <div><p>Este es un párrafo en un div.</p></div>
                    <div><p>Este es un párrafo en un div.</p></div>
                    <div><p>Este es un párrafo en un div.</p></div>
                    <div><p>Este es un párrafo en un div.</p></div>
                    <div><p>Este es un párrafo en un div.</p></div>
                    <div><p>Este es un párrafo en un div.</p></div>
                </div>
            </div>
        </div>

        """
        iframe = folium.IFrame(html=html, width=300, height=220)

        # folium.CircleMarker(location=[coord[0], coord[1]], fill_color='#43d9de', radius=8, popup=coord[2][0]).add_to(_map)
        folium.CircleMarker(location=[coord[0], coord[1]], fill_color='#43d9de', radius=8, popup=folium.Popup(iframe)).add_to(_map)

    return _map._repr_html_()

if __name__ == '__main__':
    app.run()