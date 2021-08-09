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

        <div class="container">

    <div class="line-chart-block block">
     <div class="line-chart">
       <div class='grafico'>
       <ul class='eje-y'>
         <li data-ejeY='50'></li>
         <li data-ejeY='20'></li>
         <li data-ejeY='10'></li>
         <li data-ejeY='0'></li>
       </ul>
       <ul class='eje-x'>
         <li>Apr</li>
         <li>May</li>
         <li>Jun</li>
       </ul>
         <span data-valor='25'>
           <span data-valor='8'>
             <span data-valor='13'>
               <span data-valor='5'>   
                 <span data-valor='23'>   
                 <span data-valor='12'>
                     <span data-valor='15'>
                     </span></span></span></span></span></span></span>
        </div>
       
     </div>
                    
    </div>

        """
        iframe = folium.IFrame(html=html, width=350, height=350)

        # folium.CircleMarker(location=[df["latitude"][i],df["longitude"][i]], fill_color="#FF0000", radius=8, tooltip=df["NOM_COMUNA"][i], popup=folium.Popup(iframe)).add_to(_map)

        popup = folium.Popup(iframe, max_width=2650)
        folium.Marker(
            location=[df["latitude"][i],df["longitude"][i]],
            popup=popup,
            tooltip="<strong>Temperatura actual: </strong>" + str(round(float((df["2020_12"][i])), 2)) + "°",
            icon=folium.DivIcon(html=f"""
                <div><svg>
                    <circle cx='30' cy='30' r='10' fill='""" + df["Simbología"][i] + """' opacity='1'/> 
                </svg></div>""")
        ).add_to(_map)

    folium.LayerControl().add_to(_map)

    return _map._repr_html_()

if __name__ == '__main__':
    app.run()