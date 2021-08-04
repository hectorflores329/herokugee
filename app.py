import folium
from flask import Flask


app = Flask(__name__)

@app.route('/')
def mapa():
    
    
    m = folium.Map(
        location=[-33.48621795345005, -70.66557950912359],
        zoom_start=8,
        control_scale=True
    )

    return m._repr_html_()


if __name__ == '__main__':
    app.run()
