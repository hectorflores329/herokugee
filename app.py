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

    if (comuna == 0):
        puntos = "http://ide.dataintelligence-group.com/mapasdi/temperatura/13101.csv"
    else:
        puntos = "http://ide.dataintelligence-group.com/mapasdi/temperatura/" + str(comuna) + ".csv"

    df = pd.read_csv(puntos, nrows=1000)

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
    
    for i, index in df.iterrows():
        html="""
        
        <style>

            .chart-wrap {
                --chart-width:400px;
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
                margin-left:0%;
                padding:10px;
                display:inline-block;
                white-space:nowrap;
            }

            .grid{
                margin-top:-230px;
            }
        </style>

        <div class="chart-wrap horizontal">
            <div class="title"><strong><center>TEMPERATURA 2000 - 2020</center></strong></div>
            <br>
            <div class="title"><strong>REGIÓN: </strong>""" + df["NOM_REGION"][i] + """</div>
            <div class="title"><strong>COMUNA: </strong>""" + df["NOM_COMUNA"][i] + """</div>
            <br>
            <div class="grid">
                <div class='bar' style='--bar-value:""" + str(df["2020_01"][i]) + """%;' data-name='"""+ str(round(float(df["2020_01"][i]), 1)) + """' title='"""+ str(round(float(df["2020_01"][i]), 1)) + """'></div>
                <div class='bar' style='--bar-value:""" + str(df["2020_02"][i]) + """%;' data-name='""" + str(round(float(df["2020_02"][i]), 1)) + """' title='""" + str(round(float(df["2020_02"][i]), 1)) + """'></div>
                <div class='bar' style='--bar-value:""" + str(df["2020_03"][i]) + """%;' data-name='""" + str(round(float(df["2020_03"][i]), 1)) + """' title='""" + str(round(float(df["2020_03"][i]), 1)) + """'></div>
                <div class='bar' style='--bar-value:""" + str(df["2020_04"][i]) + """%;' data-name='""" + str(round(float(df["2020_04"][i]), 1)) + """' title='""" + str(round(float(df["2020_04"][i]), 1)) + """'></div>
                <div class='bar' style='--bar-value:""" + str(df["2020_05"][i]) + """%;' data-name='""" + str(round(float(df["2020_05"][i]), 1)) + """' title='""" + str(round(float(df["2020_05"][i]), 1)) + """'></div>
                <div class='bar' style='--bar-value:""" + str(df["2020_06"][i]) + """%;' data-name='""" + str(round(float(df["2020_06"][i]), 1)) + """' title='""" + str(round(float(df["2020_06"][i]), 1)) + """'></div>
                <div class='bar' style='--bar-value:""" + str(df["2020_07"][i]) + """%;' data-name='""" + str(round(float(df["2020_07"][i]), 1)) + """' title='""" + str(round(float(df["2020_07"][i]), 1)) + """'></div>
                <div class='bar' style='--bar-value:""" + str(df["2020_08"][i]) + """%;' data-name='""" + str(round(float(df["2020_08"][i]), 1)) + """' title='""" + str(round(float(df["2020_08"][i]), 1)) + """'></div>
                <div class='bar' style='--bar-value:""" + str(df["2020_09"][i]) + """%;' data-name='""" + str(round(float(df["2020_09"][i]), 1)) + """' title='""" + str(round(float(df["2020_09"][i]), 1)) + """'></div>
                <div class='bar' style='--bar-value:""" + str(df["2020_10"][i]) + """%;' data-name='""" + str(round(float(df["2020_10"][i]), 1)) + """' title='""" + str(round(float(df["2020_10"][i]), 1)) + """'></div>
                <div class='bar' style='--bar-value:""" + str(df["2020_11"][i]) + """%;' data-name='""" + str(round(float(df["2020_11"][i]), 1)) + """' title='""" + str(round(float(df["2020_11"][i]), 1)) + """'></div>
                <div class='bar' style='--bar-value:""" + str(df["2020_12"][i]) + """%;' data-name='""" + str(round(float(df["2020_12"][i]), 1)) + """' title='""" + str(round(float(df["2020_12"][i]), 1)) + """'></div>
            </div>
        </div>

        """
        iframe = folium.IFrame(html=html, width=450, height=300)

        # folium.CircleMarker(location=[df["latitude"][i],df["longitude"][i]], fill_color="#FF0000", radius=8, tooltip=df["NOM_COMUNA"][i], popup=folium.Popup(iframe)).add_to(_map)

        popup = folium.Popup(iframe, max_width=2650)
        folium.Marker(
            location=[df["latitude"][i],df["longitude"][i]],
            popup=popup,
            tooltip="<strong>Parcela ID: </strong>" + str(df["Parcela_ID"][i]) + "<br>" + 
            "<strong>Temperatura actual: </strong>" + str(round(float((df["2020_12"][i])), 1)) + "°" + 
            "<br><strong>Latitud: </strong>" + str(df["latitude"][i]) + "<br>" +
            "<strong>Longitud: </strong>" + str(df["longitude"][i]) + "<br>",
            icon=folium.DivIcon(html=f"""
                <div><svg>
                    <circle cx='30' cy='30' r='10' fill='""" + df["Simbología"][i] + """' opacity='1'/> 
                </svg></div>""")
        ).add_to(_map)


    folium.LayerControl().add_to(_map)

    return _map._repr_html_()

if __name__ == '__main__':
    app.run()