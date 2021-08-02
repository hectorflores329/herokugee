import folium
from flask import Flask
#import branca
import random

app = Flask(__name__)

@app.route('/')
def mapa():
    
    url = (
        "https://raw.githubusercontent.com/hectorflores329/herokugee/main"
    )
    mediambiente = f"{url}/elbosque2.json"

    m = folium.Map(
        location=[-33.48621795345005, -70.66557950912359],
        zoom_start=5,
        control_scale=True
        # tiles = "openstreetmap"
    )


    folium.GeoJson(mediambiente, 
                    name="Glaciares",
                    style_function = lambda feature: {
                    #'fillColor': getcolor(feature),
                    'weight': 0,
                    'fillOpacity': 0.8,},
                    tooltip = folium.GeoJsonTooltip(fields=["NOM_COM", "TEMP"],
                    aliases = ['Comuna', 'Temperatura'],
                    )
    ).add_to(m)

    return m._repr_html_()


if __name__ == '__main__':
    app.run()
