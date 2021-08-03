import folium
from flask import Flask
import branca.colormap as cm
from branca.element import Template, MacroElement
import folium.plugins as plugins

app = Flask(__name__)

@app.route('/')
def mapa():
    
    '''def downloadJson(link):
        
        with urllib.request.urlopen(link) as url:
            data = json.loads(url.read().decode())
        
        return data'''

    # spatial_temporal_data = downloadJson("https://raw.githubusercontent.com/ghandic/folium/master/examples/data/house_movement.json")

    m = folium.Map(
        location=[56.096555, -3.64746],
        tiles = 'cartodbpositron',
        zoom_start=5
    )

    '''plugins.TimestampedGeoJson(spatial_temporal_data, 
                period='P1M', add_last_point=True,
                auto_play=False, loop=False, 
                maxSpeed=1, loopButton=True,
                dateOptions='YYYY/MM/DD',
                timeSliderDragUpdate=True).add_to(m)

    return m._repr_html_()'''


if __name__ == '__main__':
    app.run()
