from flask import Flask
from folium.map import FeatureGroup, Popup
import pandas as pd
import folium
from flask import request

app = Flask(__name__)

@app.route('/')
def temp():

    try:
        periodo = request.args.get("p")
        periodo = periodo
    except:
        periodo = 0

    puntos = "http://ide.dataintelligence-group.com/mapasdi/temperatura/c13115.csv"

    df = pd.read_csv(puntos)

    latitude = df["latitude"].tolist()
    longitude = df["longitude"].tolist()
    nomCom = df["NOM_COMUNA"].tolist()

    locations = []

    for lat, lon in zip(latitude, longitude):
        fLat = float(lat)
        fLon = float(lon)
        locations.append((lat, lon, nomCom))

    if (periodo == 0):
        ubicacion = [-33.467890412071654, -70.66557950912359]
    else:
        ubicacion = [locations[0][0], locations[0][1]]
    
    _map = folium.Map(
        location=ubicacion,
        zoom_start=11,
    )
    
    for i, index in df.iterrows():


        # folium.CircleMarker(location=[df["latitude"][i],df["longitude"][i]], fill_color="#FF0000", radius=8, tooltip=df["NOM_COMUNA"][i], popup=folium.Popup(iframe)).add_to(_map)

        folium.Marker(
            location=[df["latitude"][i],df["longitude"][i]],
            icon=folium.DivIcon(html=f"""
                <div>
                    <svg>
                        <circle cx='30' cy='30' r='10' fill='""" + df[periodo][i] + """' opacity='1'/> 
                    </svg>
                </div>""")
        ).add_to(_map)


    folium.LayerControl().add_to(_map)

    return _map._repr_html_()

if __name__ == '__main__':
    app.run()