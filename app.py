import folium
from flask import Flask
import json
import requests

app = Flask(__name__)

@app.route('/')
def mapa():
    
    url = (
        "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"
    )
    vis1 = json.loads(requests.get(f"{url}/vis1.json").text)
    vis2 = json.loads(requests.get(f"{url}/vis2.json").text)
    vis3 = json.loads(requests.get(f"{url}/vis3.json").text)

    m = folium.Map(
        location=[-33.48621795345005, -70.66557950912359],
        zoom_start=8,
        control_scale=True,
    )

    folium.CircleMarker(
        location=[-32.41681831859102, -70.57579231998415],
        fill=True,
        radius=5,
        popup=folium.Popup(max_width=450).add_child(
            folium.Vega(vis1, width=450, height=250)
        ),
    ).add_to(m)

    folium.CircleMarker(
        location=[-35.346523319705604, -71.34401806293496],
        fill=True,
        radius=5,
        popup=folium.Popup(max_width=450).add_child(
            folium.Vega(vis2, width=450, height=250)
        ),
    ).add_to(m)

    folium.CircleMarker(
        location=[-37.3530323621873, -72.25758381593647],
        fill=True,
        radius=5,
        popup=folium.Popup(max_width=450).add_child(
            folium.Vega(vis3, width=450, height=250)
        ),
    ).add_to(m)

    return m._repr_html_()


if __name__ == '__main__':
    app.run()
