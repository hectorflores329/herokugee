import folium
from flask import Flask
import branca.colormap as cm
from branca.element import Template, MacroElement
import folium.plugins as plugins
import urllib.request, json 

app = Flask(__name__)

@app.route('/')
def mapa():
    
    def downloadJson(link):
        
        with urllib.request.urlopen(link) as url:
            data = json.loads(url.read().decode())
        
        return data

    spatial_temporal_data = downloadJson("https://raw.githubusercontent.com/hectorflores329/herokugee/main/table.geojson")

    m = folium.Map(
        location=[-33.48621795345005, -70.66557950912359],
        tiles = 'cartodbpositron',
        zoom_start=5
    )

    plugins.TimestampedGeoJson(spatial_temporal_data, 
                period='P1M', 
                add_last_point=True,
                auto_play=False, 
                loop=True, 
                ).add_to(m)

    return m._repr_html_()


if __name__ == '__main__':
    app.run()
