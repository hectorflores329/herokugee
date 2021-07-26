import ee
import geemap

def mapa():
    Map = geemap.Map(center=(40, -100), zoom=4)
    Map

if __name__ == '__main__':
    mapa()
