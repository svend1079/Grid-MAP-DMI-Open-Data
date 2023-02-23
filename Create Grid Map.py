# Import neccesary packages
import folium
from folium import features
import json
from folium.plugins import Geocoder
import requests

m = folium.Map(tiles='https://a.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}@2x.png', attr='CartoDB, Voyager',
               zoom_control=False, zoom_start=7.4,
               location=[56.05, 10.84])

with open("C:/Users/B056860/Downloads/10x10km-Grid (3)/10x10km.geojson") as f:
    grid10x10 = json.load(f)
with open("C:/Users/B056860/Downloads/20x20km-Grid (2)/20x20km.geojson") as f:
    grid20x20 = json.load(f)
with open("C:/Users/B056860/Desktop/Map_test/Kommuner.geojson") as f:
    kommuner = json.load(f)

style_function_20 = {'fillOpacity': '0.1', 'color': '#0066ff', 'weight': '1.5'}
style_function_10 = {'fillOpacity': '0.1', 'color': '#248f8f', 'weight': '1'}
style_function_kom = {'fillOpacity': '0.1', 'color': '#f73f3f', 'weight': '1'}

g20 = folium.GeoJson(grid20x20, name='20x20km', style_function=lambda x: style_function_20)
g20.add_child(folium.features.GeoJsonPopup(fields=['cellId']))
g10 = folium.GeoJson(grid10x10, name='10x10km', style_function=lambda x: style_function_10)
g10.add_child(folium.features.GeoJsonPopup(fields=['cellId']))
kom_feat = folium.GeoJson(kommuner, name='Kommuner', style_function=lambda x: style_function_kom)
kom_feat.add_child(folium.features.GeoJsonPopup(fields=('Kommune', 'KommuneID')))

g20.add_to(m).show = False
g10.add_to(m).show = False
kom_feat.add_to(m).show = False
Geocoder(add_marker=True).add_to(m)

lay = folium.LayerControl(position='topleft', collapsed=False)
lay.add_to(m)

m.save(r'C:/Users/B056860/Desktop/Map_test/DMI Grid and Municipalities.html')

