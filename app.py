import pandas as pd # library for data analsysis
import json # library to handle JSON files
from geopy.geocoders import Nominatim # convert an address into latitude and longitude values
import requests # library to handle requests
import folium # map rendering library
import numpy as np
import streamlit as st
from streamlit_folium import folium_static

def findObject(valueToFind, listOfValue):
    for obj in listOfValue['CVEGEO']:
        if valueToFind in obj :
            print("Encontrado")


# SIDEBAR
st.markdown('<style>' + open('./styles/style.css').read() + '</style>', unsafe_allow_html=True)
data_2020 = pd.read_csv('./resources/urbanlud2020_sin_servicios.csv')
data_2030 = pd.read_csv('./resources/urbanlud2030.csv', index_col ="CVEGEO")
data_geo = json.load(open('./resources/AGEBS.geojson'))

for idx, data in enumerate(data_geo['features']):
    CVEGEO = data['properties']['CVEGEO']
    dataframeRow = data_2020[data_2020['CVEGEO'] == CVEGEO]
    if dataframeRow is None:
        data_geo['features'][idx]['properties']['clusters'] = dataframeRow['clusters'].values[0]
    

st.title('Urbanlud Map')
mapa_2020 = folium.Map(tiles='OpenStreetMap', location=[20.838060, -103.602699, ], zoom_start=10)
maps = folium.Choropleth(
    geo_data = data_geo,
    data = data_2020,
    columns=['CVEGEO', 'clusters'],
    key_on='feature.properties.CVEGEO',
    fill_color='BuPu', 
    fill_opacity=0.7, 
    line_opacity=0.2,
    highlight=True,
    reset=True
).add_to(mapa_2020)

folium.LayerControl().add_to(mapa_2020)
maps.geojson.add_child(folium.features.GeoJsonTooltip(fields=['clusters'], aliases=['ID AGEBS: '], labels=True))   
folium_static(mapa_2020)




