import folium
from flask import Flask
import branca.colormap as cm
from branca.element import Template, MacroElement
import folium.plugins as plugins

app = Flask(__name__)

@app.route('/')
def mapa():
    
    m = folium.Map(location=[52.467697, -2.548828], zoom_start=6)

    polygon = {
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
                'times': ['2015-07-22T00:00:00', '2015-08-22T00:00:00', '2015-09-22T00:00:00']
            }
        }

    plugins.TimestampedGeoJson(
        {'type': 'FeatureCollection', 'features': [polygon]},
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
