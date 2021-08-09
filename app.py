from flask import Flask
from folium.map import FeatureGroup, Popup
import pandas as pd
import folium
from flask import request
from folium.plugins import FastMarkerCluster

app = Flask(__name__)

@app.route('/')
def temp():

    try:
        comuna = request.args.get("comuna")
        comuna = int(comuna)
    except:
        comuna = 0

    puntos = "http://ide.dataintelligence-group.com/mapasdi/temperatura_2020.csv"
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

    if (comuna == 0):
        ubicacion = [-33.467890412071654, -70.66557950912359]
    else:
        ubicacion = [locations[0][0], locations[0][1]]
    
    _map = folium.Map(
        location=ubicacion,
        zoom_start=11,
    )

    texto1 = "2020"
    valor1 = "35"

    texto2 = "2021111"
    valor2 = "90"
    
    for i, index in df.iterrows():
        html="""
        
        <style>

            .chart-wrap {
                --chart-width:220px;
                --grid-color:#aaa;
                --bar-color:#F16335;
                --bar-thickness:30px;
                --bar-rounded: 3px;
                --bar-spacing:3px;
                font-family:sans-serif;
                width:var(--chart-width);
            }

            .chart-wrap.horizontal .grid{
                transform:rotate(-90deg);
            }

            .chart-wrap.horizontal .bar::after{
                transform: rotate(60deg);
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
            <div class="title">""" + df["NOM_COMUNA"][i] + """</div>
            <br>
            <div class="grid">
                <div class='bar' style='--bar-value:""" + valor1 + """%;' data-name='""" + texto1 +"""' title='""" + texto1 +""" 85%'></div>
                <div class='bar' style='--bar-value:%;' data-name='2015' title='2015 23%'></div>
                <div class='bar' style='--bar-value:7%;' data-name='2016' title='2016 7%'></div>
                <div class='bar' style='--bar-value:38%;' data-name='2017' title='2017 38%'></div>
                <div class='bar' style='--bar-value:35%;' data-name='2018' title='2018 35%'></div>
                <div class='bar' style='--bar-value:30%;' data-name='2019' title='2019 30%'></div>
                <div class='bar' style='--bar-value:5%;' data-name='2020' title='2020 5%'></div>
                <div class='bar' style='--bar-value:""" + valor2 + """%;' data-name='""" + texto2 +"""' title='""" + texto2 +""" 20%'></div>
            </div>
        </div>

        """
        iframe = folium.IFrame(html=html, width=350, height=350)

        # folium.CircleMarker(location=[coord[0], coord[1]], fill_color='#43d9de', radius=8, popup=coord[2][0]).add_to(_map)
        # folium.CircleMarker(location=[df["latitude"][i],df["longitude"][i]], fill_color=df["Simbología"][i], radius=8, tooltip=df["NOM_COMUNA"][i], popup=folium.Popup(iframe)).add_to(_map)
        _map.add_child(FastMarkerCluster(df["latitude"][i],df["longitude"][i]))

    return _map._repr_html_()

if __name__ == '__main__':
    app.run()