from flask import Flask
from folium.map import FeatureGroup, Popup
import pandas as pd
import folium

app = Flask(__name__)

@app.route('/')
def temp():

    puntos = "https://raw.githubusercontent.com/hectorflores329/herokugee/main/Regi%C3%B3n%20Metropolitana%20de%20Santiago%2C%20TEMP.csv"
    df = pd.read_csv(puntos)

    latitude = df["latitude"].tolist()
    longitude = df["longitude"].tolist()
    id = df["Parcela_ID"].tolist()

    locations = []

    for lat, lon in zip(latitude, longitude):
        fLat = float(lat)
        fLon = float(lon)
        locations.append([lat,lon])

    _map = folium.Map(
        location=[-33.467890412071654, -70.66557950912359],
        zoom_start=4,
        )

    _featureGroup = folium.FeatureGroup(name="Puntos de temperatura")
    marcadores = folium.MarkerCluster(locations = locations, popups = id)
    marcadores.add_to(_featureGroup)

    _map.add_child(_featureGroup)
    folium.LayerControl().add_to(_map)

    return _map._repr_html_()

if __name__ == '__main__':
    app.run()