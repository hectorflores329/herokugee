import ee
import geemap

from flask import Flask
import folium

app = Flask(__name__)

@app.route('/')
def mapa():

    ee.Initialize()

    # Load the Sentinel-1 ImageCollection
    sentinel1 = ee.ImageCollection('COPERNICUS/S1_GRD')

                # Filter to get images with VV and VH dual polarization.
    vh = (sentinel1.filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VV'))
                .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VH'))
                # Filter to get images collected in interferometric wide swath mode.
                .filter(ee.Filter.eq('instrumentMode', 'IW')))

    # Filter to get images from different look angles.
    vhAscending = vh.filter(ee.Filter.eq('orbitProperties_pass', 'ASCENDING'))
    vhDescending = vh.filter(ee.Filter.eq('orbitProperties_pass', 'DESCENDING'))

    # Create a composite from means at different polarizations and look angles.
    composite = ee.Image.cat([
    vhAscending.select('VH').mean(),
    ee.ImageCollection(vhAscending.select('VV').merge(vhDescending.select('VV'))).mean(),
    vhDescending.select('VH').mean()
    ]).focal_median()

    # Display as a composite of polarization and backscattering characteristics.

    # Define a method for displaying Earth Engine image tiles to folium map.
    def add_ee_layer(self, ee_image_object, vis_params, name):
        map_id_dict = ee.Image(ee_image_object).getMapId(vis_params) # STUCK
        folium.raster_layers.TileLayer(
            tiles = map_id_dict['tile_fetcher'].url_format,
            attr = "Map Data © Google Earth Engine",
            name = name,
            overlay = True,
        control = True
    ).add_to(self)

    # Add EE drawing method to folium.
    folium.Map.add_ee_layer = add_ee_layer

    m = folium.Map(location=[-33.48621795345005, -70.66557950912359], zoom_start=4)

    return m._repr_html_()
    # return HeatMapWithTime(lat_long_list2,radius=5,auto_play=True,position='bottomright').add_to(map)

if __name__ == '__main__':
    app.run()
