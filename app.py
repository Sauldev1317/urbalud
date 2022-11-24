import pandas as pd # library for data analsysis
import json # library to handle JSON files
from geopy.geocoders import Nominatim # convert an address into latitude and longitude values
import requests # library to handle requests
import folium # map rendering library
import numpy as np
import streamlit as st
from streamlit_folium import folium_static
from st_on_hover_tabs import on_hover_tabs
st.set_page_config(layout="wide")

def center():
    address = 'Surabaya, ID'
    geolocator = Nominatim(user_agent="id_explorer")
    location = geolocator.geocode(address)
    latitude = location.latitude
    longitude = location.longitude
    return latitude, longitude

def threshold(data, data_all):
    threshold_scale = np.linspace(data_all['Areas Region(km squared)'].min(),
                              data_all['Areas Region(km squared)'].max(),
                              10, dtype=float)
    threshold_scale = threshold_scale.tolist() # change the numpy array to a list
    threshold_scale[-1] = threshold_scale[-1]
    return threshold_scale

def show_maps(data, threshold_scale, data_all, data_geo):
    maps= folium.Choropleth(
        geo_data = data_geo,
        data = data_all,
        columns=['CVEGEO'],
        key_on='feature.properties.CVEGEO',
        fill_color='YlOrRd', 
        fill_opacity=0.7, 
        line_opacity=0.2,
    ).add_to(map_sby)

    folium.LayerControl().add_to(map_sby)                                             
    folium_static(map_sby)

# SIDEBAR
st.markdown('<style>' + open('./styles/style.css').read() + '</style>', unsafe_allow_html=True)
data_2020 = pd.read_csv('./resources/urbanlud2020.csv')
data_2030 = pd.read_csv('./resources/urbanlud2030.csv')
data_geo = json.load(open('./resources/AGEBS.geojson'))
centers = center()

with st.sidebar:
    tabs = on_hover_tabs(tabName=['Urbanlud Demo'], 
                         iconName=['dashboard'], default_choice=0)

if tabs == 'Urbanlud Demo':
    st.title('Urbanlud Map')

    st.write('Mapa del año 2020')
    mapa_2020 = folium.Map(tiles='OpenStreetMap', location=[20.838060, -103.602699, ], zoom_start=10,  width=700, height=400)
    folium.Choropleth(
        geo_data = data_geo,
        data = data_2020,
        columns=['CVEGEO', 'clusters'],
        key_on='feature.properties.CVEGEO',
        fill_color='BuPu', 
        fill_opacity=0.7, 
        line_opacity=0.2
    ).add_to(mapa_2020)
    folium.LayerControl().add_to(mapa_2020)
    folium_static(mapa_2020)
    
    mapa_2030 = folium.Map(tiles='OpenStreetMap', location=[20.838060, -103.602699, ], zoom_start=10,  width=700, height=400)
    folium.Choropleth(
        geo_data = data_geo,
        data = data_2030,
        columns=['CVEGEO', 'clusters'],
        key_on='feature.properties.CVEGEO',
        fill_color='BuPu', 
        fill_opacity=0.7, 
        line_opacity=0.2
    ).add_to(mapa_2030)
    folium.LayerControl().add_to(mapa_2030)
    folium_static(mapa_2030)




