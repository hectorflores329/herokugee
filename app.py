import folium
from flask import Flask
import branca

app = Flask(__name__)

@app.route('/')
def mapa():
    
    m = folium.Map(location=[-33.48621795345005, -70.66557950912359], zoom_start=4)
    
    # folium.Marker([-33.48621795345005, -70.66557950912359], popup='Plaza Mayor').add_to(m)

    html = "<p>Latitud: 40.0</p><p>Longitud: 2.1</p>"
    iframe1 = branca.element.IFrame(html=html, width=250, height=200)
    html = "<p>Latitud: 40.0</p><p>Longitud: 3.5</p>"
    iframe2 = branca.element.IFrame(html=html, width=250, height=200)
    html = "<p>Latitud: 39.0</p><p>Longitud: 2.1</p>"
    iframe3 = branca.element.IFrame(html=html, width=250, height=200)
    html = "<p>Latitud: 39.0</p><p>Longitud: 3.5</p>"
    iframe4 = branca.element.IFrame(html=html, width=250, height=200)

    marcador1 = folium.Marker(
        location=(-33.2993248483003, -70.84960050794211),
        popup=folium.Popup(iframe1, max_width=500),
        icon=folium.Icon(color="black")
    )
    marcador2 = folium.Marker(
        location=(-33.62240730758864, -70.84960050794211),
        popup=folium.Popup(iframe2, max_width=500),
        icon=folium.Icon(color="gray")
    )
    marcador3 = folium.Marker(
        location=(-33.560633705782394, -70.43761319983437),
        popup=folium.Popup(iframe3, max_width=500),
        icon=folium.Icon(color="black")
    )
    marcador4 = folium.Marker(
        location=(-33.2844019692712, -70.45821256523976),
        popup=folium.Popup(iframe4, max_width=500),
        icon=folium.Icon(color="gray")
    )

    # Creamos dos grupos para los marcadores
    grp_este = folium.FeatureGroup(name='Grupo 1')
    grp_oeste = folium.FeatureGroup(name='Grupo 2')
    # Añadimos los marcadores AL GRUPO AL QUE CORRESPONDAN (NO AL MAPA)
    marcador1.add_to(grp_oeste)
    marcador2.add_to(grp_este)
    marcador3.add_to(grp_oeste)
    marcador4.add_to(grp_este)
    # Y ahora añadimos los grupos al mapa
    grp_este.add_to(m)
    grp_oeste.add_to(m)
    # Y añadimos, además, el control de capas
    folium.LayerControl().add_to(m)

    # Get a composite of all Sentinal 2 images within a date range that include my point of interest.
    #point = ee.Geometry.Point([-82.4572, 27.9506])
    
    return m._repr_html_()


if __name__ == '__main__':
    app.run()
