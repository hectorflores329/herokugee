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

    latlon = [ (51.249443914705175, -0.13878830247011467), (51.249443914705175, -0.13878830247011467), (51.249768239976866, -2.8610415615063034), (52.249768239976866, -2.8610415615063034), (54.249768239976866, -2.8610415615063034)]
    mapit = folium.Map( location=[52.667989, -1.464582], zoom_start=6 )
    for coord in latlon:
        folium.CircleMarker( location=[ coord[0], coord[1] ], fill_color='#43d9de', radius=8, popup="Hola" ).add_to( mapit )

    return mapit._repr_html_()

if __name__ == '__main__':
    app.run()