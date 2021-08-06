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

            .chart-wrap {
                --chart-width:420px;
                --grid-color:#aaa;
                --bar-color:#F16335;
                --bar-thickness:40px;
                --bar-rounded: 3px;
                --bar-spacing:10px;
                font-family:sans-serif;
                width:var(--chart-width);
            }

            .chart-wrap.horizontal .grid{
                transform:rotate(-90deg);
            }

            .chart-wrap.horizontal .bar::after{
                transform: rotate(45deg);
                padding-top:0px;
                display: block;
            }

            .chart-wrap .bar {
                width: var(--bar-value);
                height:var(--bar-thickness);
                margin:var(--bar-spacing) 0;
                background-color:var(--bar-color);
                border-radius:0 var(--bar-rounded) var(--bar-rounded) 0;
            }
        
            .chart-wrap .bar::after{
                content:attr(data-name);
                margin-left:100%;
                padding:10px;
                display:inline-block;
                white-space:nowrap;
            }

        </style>

        <div class="chart-wrap horizontal">
            <div><p>""" + coord[2][0] + """</p></div>
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

        """
        iframe = folium.IFrame(html=html, width=300, height=220)

        # folium.CircleMarker(location=[coord[0], coord[1]], fill_color='#43d9de', radius=8, popup=coord[2][0]).add_to(_map)
        folium.CircleMarker(location=[coord[0], coord[1]], fill_color='#43d9de', radius=8, popup=folium.Popup(iframe)).add_to(_map)

    return _map._repr_html_()

if __name__ == '__main__':
    app.run()