import folium
from flask import Flask
import branca.colormap as cm
from branca.element import Template, MacroElement
import folium.plugins as plugins

app = Flask(__name__)

@app.route('/')
def mapa():
    
    url = (
        "https://raw.githubusercontent.com/hectorflores329/herokugee/main"
    )
    mediambiente = f"{url}/table.geojson"

    m = folium.Map(
        location=[-33.48621795345005, -70.66557950912359],
        zoom_start=8,
        control_scale=True
        # tiles = "openstreetmap"
    )

    plugins.TimestampedGeoJson(
        {"type": "FeatureCollection", "features": mediambiente},
        period="P1M",
        add_last_point=True,
        auto_play=False,
        loop=False,
        max_speed=1,
        loop_button=True,
        date_options="YYYY/MM/DD",
        time_slider_drag_update=True,
        duration="P2M",
    ).add_to(m)

    def getcolor(feature):
        if feature['properties']['median'] >= 20.0 and feature['properties']['median'] <= 30.0:
            return '#ffbd48'
        if feature['properties']['median'] >= 31.0 and feature['properties']['median'] <= 35.0:
            return '#ff8548'
        if feature['properties']['median'] >= 36.0 and feature['properties']['median'] <= 40.0:
            return '#ff4848'
        else:
            return 'transparent'

    folium.GeoJson(mediambiente, 
                    name="Temperatura",
                    style_function = lambda feature: {
                    'fillColor': getcolor(feature),
                    'weight': 1,
                    'color': 'black',
                    'weight': '2',
                    'fillOpacity': 0.8,},
                    tooltip = folium.GeoJsonTooltip(fields=["Nom_com", "median"],
                    aliases = ['Comuna', 'Temperatura'],
                    )
    ).add_to(m)

    template = """
    {% macro html(this, kwargs) %}

    <!doctype html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Dataintelligence</title>
    <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">

    <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
    <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
    
    <script>
    $( function() {
        $( "#maplegend" ).draggable({
                        start: function (event, ui) {
                            $(this).css({
                                right: "auto",
                                top: "auto",
                                bottom: "auto"
                            });
                        }
                    });
    });

    </script>
    </head>
    <body>

    
    <div id='maplegend' class='maplegend' 
        style='position: absolute; z-index:9999; border:2px solid grey; background-color:rgba(255, 255, 255, 0.8);
        border-radius:6px; padding: 10px; font-size:14px; right: 20px; bottom: 20px;'>
        
    <div class='legend-title'>Temperatura</div>
    <div class='legend-scale'>
    <ul class='legend-labels'>
        <li><span style='background:#ffbd48;opacity:0.7;'></span>20° - 30°</li>
        <li><span style='background:#ff8548;opacity:0.7;'></span>31° -35°</li>
        <li><span style='background:#ff4848;opacity:0.7;'></span>36° - 40°</li>

    </ul>
    </div>
    </div>
    
    </body>
    </html>

    <style type='text/css'>
    .maplegend .legend-title {
        text-align: left;
        margin-bottom: 5px;
        font-weight: bold;
        font-size: 90%;
        }
    .maplegend .legend-scale ul {
        margin: 0;
        margin-bottom: 5px;
        padding: 0;
        float: left;
        list-style: none;
        }
    .maplegend .legend-scale ul li {
        font-size: 80%;
        list-style: none;
        margin-left: 0;
        line-height: 18px;
        margin-bottom: 2px;
        }
    .maplegend ul.legend-labels li span {
        display: block;
        float: left;
        height: 16px;
        width: 30px;
        margin-right: 5px;
        margin-left: 0;
        border: 1px solid #999;
        }
    .maplegend .legend-source {
        font-size: 80%;
        color: #777;
        clear: both;
        }
    .maplegend a {
        color: #777;
        }
    </style>
    {% endmacro %}"""

    macro = MacroElement()
    macro._template = Template(template)

    m.get_root().add_child(macro)

    return m._repr_html_()


if __name__ == '__main__':
    app.run()
