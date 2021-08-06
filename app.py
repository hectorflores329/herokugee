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
        <div class="chart-wrap horizontal">
        <div class="title">TEMPERATURA: """ + coord[2] + """</div>
            <br>
            <div class="grid">

                <div class="bar" style="--bar-value:85%;" data-name="Your Blog" title="Your Blog 85%"></div>
                <div class="bar" style="--bar-value:23%;" data-name="Medium" title="Medium 23%"></div>
                <div class="bar" style="--bar-value:7%;" data-name="Tumblr" title="Tumblr 7%"></div>
                <div class="bar" style="--bar-value:38%;" data-name="Facebook" title="Facebook 38%"></div>
                <div class="bar" style="--bar-value:35%;" data-name="YouTube" title="YouTube 35%"></div>
                <div class="bar" style="--bar-value:30%;" data-name="LinkedIn" title="LinkedIn 30%"></div>
                <div class="bar" style="--bar-value:5%;" data-name="Twitter" title="Twitter 5%"></div>
                <div class="bar" style="--bar-value:20%;" data-name="Other" title="Other 20%"></div>
                

            </div>
        </div>
        """
        iframe = folium.IFrame(html=html, width=200, height=100)

        # folium.CircleMarker(location=[coord[0], coord[1]], fill_color='#43d9de', radius=8, popup=coord[2][0]).add_to(_map)
        folium.CircleMarker(location=[coord[0], coord[1]], fill_color='#43d9de', radius=8, popup=folium.Popup(iframe)).add_to(_map)

    return _map._repr_html_()

if __name__ == '__main__':
    app.run()