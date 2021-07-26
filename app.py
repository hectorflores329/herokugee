import ee
import geemap

from flask import Flask
import folium

app = Flask(__name__)

@app.route('/')
def mapa():
    
    def add_ee_layer(self, ee_image_object, vis_params, name):
        map_id_dict = ee.Image(ee_image_object).getMapId(vis_params)
        folium.raster_layers.TileLayer(
            tiles=map_id_dict['tile_fetcher'].url_format,
            attr='Map Data &copy; <a href="https://earthengine.google.com/">Google Earth Engine</a>',
            name=name,
            overlay=True,
            control=True
        ).add_to(self)

    folium.Map.add_ee_layer = add_ee_layer

    m = folium.Map(location=[-33.48621795345005, -70.66557950912359], zoom_start=4)

    return m._repr_html_()
    # return HeatMapWithTime(lat_long_list2,radius=5,auto_play=True,position='bottomright').add_to(map)

if __name__ == '__main__':
    app.run()
