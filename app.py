import folium
from flask import Flask
#import branca
import random

app = Flask(__name__)

@app.route('/')
def mapa():
    
    m = folium.Map(location=[-33.48621795345005, -70.66557950912359], zoom_start=4)
    
    def randome_points(amount, LON_min, LON_max, LAT_min, LAT_max):

        points = []
        for _ in range(amount):
            points.append(
                (random.uniform(LON_min, LON_max), random.uniform(LAT_min, LAT_max))
            )

        return points

    def create_envelope_polygon(
        map_object, list_of_points, layer_name, line_color, fill_color, weight, text
    ):

        # Since it is pointless to draw a box around less than 2 points check len of input
        if len(list_of_points) < 2:
            return

        # Find the edges of box
        from operator import itemgetter

        list_of_points = sorted(list_of_points, key=itemgetter(0))
        x_min = list_of_points[0]
        x_max = list_of_points[len(list_of_points) - 1]

        list_of_points = sorted(list_of_points, key=itemgetter(1))
        y_min = list_of_points[0]
        y_max = list_of_points[len(list_of_points) - 1]

        upper_left = (x_min[0], y_max[1])
        upper_right = (x_max[0], y_max[1])
        lower_right = (x_max[0], y_min[1])
        lower_left = (x_min[0], y_min[1])

        edges = [upper_left, upper_right, lower_right, lower_left]

        # Create feature group, add the polygon and add the feature group to the map
        fg = folium.FeatureGroup(name=layer_name)
        fg.add_child(
            folium.vector_layers.Polygon(
                locations=edges,
                color=line_color,
                fill_color=fill_color,
                weight=weight,
                popup=(folium.Popup(text)),
            )
        )
        map_object.add_child(fg)

        return map_object

    list_of_points = randome_points(
        amount=10, LON_min=49.1, LON_max=50, LAT_min=8, LAT_max=9
    )

    create_envelope_polygon(
        m,
        list_of_points,
        layer_name="Example envelope",
        line_color="indianred",
        fill_color="red",
        weight=5,
        text="Example envelope",
    )

    return m._repr_html_()


if __name__ == '__main__':
    app.run()
