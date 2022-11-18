import pandas as pd # library for data analsysis
import json # library to handle JSON files
from geopy.geocoders import Nominatim # convert an address into latitude and longitude values
import requests # library to handle requests
import numpy as np
import folium # map rendering library
import streamlit as st
from streamlit_folium import folium_static




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
        columns=['District', 'Areas Region(km squared)'],
        key_on='feature.properties.name',
        threshold_scale=threshold_scale,
        fill_color='YlOrRd', 
        fill_opacity=0.7, 
        line_opacity=0.2,
        legend_name= 'Areas Region(km squared)',
        highlight=True,
        reset=True).add_to(map_sby)

    folium.LayerControl().add_to(map_sby)
    maps.geojson.add_child(folium.features.GeoJsonTooltip(fields=['name',data], aliases=['District: ', 'Areas Region(km squared)'], labels=True))                                                       
    folium_static(map_sby)


def urbaludDemoPage():
    data_all = pd.read_csv('./resources/Surabaya_Full_of_Data.csv')
    data_geo = json.load(open('./resources/Kecamatan_Surabaya.geojson'))
    centers = center()
    map_sby = folium.Map(tiles='OpenStreetMap', location=[centers[0], centers[1]], zoom_start=12)
    st.title('Map of Surabaya')

    data_all['District'] = data_all['District'].str.title()
    data_all = data_all.replace({'District':'Pabean Cantikan'},'Pabean Cantian')
    data_all = data_all.replace({'District':'Karangpilang'},'Karang Pilang')

    for idx in range(31):
        data_geo['features'][idx]['properties']['Total_Pop'] = int(data_all['Total Population'][idx])
        data_geo['features'][idx]['properties']['Male_Pop'] = int(data_all['Male Population'][idx])
        data_geo['features'][idx]['properties']['Female_Pop'] = int(data_all['Female Population'][idx])
        data_geo['features'][idx]['properties']['Area_Region'] = float(data_all['Areas Region(km squared)'][idx])
    show_maps('Area_Region', threshold('Area_Region',data_all ), data_all, data_geo)
