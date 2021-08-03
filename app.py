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

    m = folium.Map(location=[52.467697, -2.548828], zoom_start=6)

    polygon_1 = {
        'type': 'Feature',
        'geometry': {
            'type': 'MultiPolygon',
            'coordinates': [((
                (-2.548828, 51.467697),
                (-0.087891, 51.536086),
                (-1.516113, 53.800651),
                (-6.240234, 53.383328),
            ),)],
        },
        'properties': {
            'style': {
                'color': 'blue',
            },
            'times': ['2015-07-22T00:00:00', '2015-08-22T00:00:00',
                    '2015-09-22T00:00:00', '2015-10-22T00:00:00',
                    '2015-11-22T00:00:00', '2015-12-22T00:00:00']
        }
    }

    polygon_2 = {
        'type': 'Feature',
        'geometry': {
            'type': 'MultiPolygon',
            'coordinates': [((
                (-3.548828, 50.467697),
                (-1.087891, 50.536086),
                (-2.516113, 52.800651),
                (-7.240234, 52.383328),
            ),)],
        },
        'properties': {
            'style': {
                'color': 'yellow',
            },
            'times': ['2015-07-22T00:00:00', '2015-08-22T00:00:00']
        }
    }

    plugins.TimestampedGeoJson(
        {'type': 'FeatureCollection', 'features': [polygon_1, polygon_2]},
        period='P1M',
        duration='P1M',
        auto_play=False,
        loop=False,
        loop_button=True,
        date_options='YYYY/MM/DD',
    ).add_to(m)

    return m._repr_html_()


if __name__ == '__main__':
    app.run()
