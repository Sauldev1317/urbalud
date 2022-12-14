import pandas as pd # library for data analsysis
import json # library to handle JSON files
from geopy.geocoders import Nominatim # convert an address into latitude and longitude values
import requests # library to handle requests
import folium # map rendering library
import numpy as np
import streamlit as st
from streamlit_folium import folium_static
st.set_page_config(layout="wide")
st.markdown('<style>' + open('./styles/style.css').read() + '</style>', unsafe_allow_html=True)
datos_2020 = pd.read_csv('./resources/datos_2020.csv')
datos_2030 = pd.read_csv('./resources/datos_2030.csv')

def loadData2020() :
    data_geo_2020 = json.load(open('./resources/AGEBS2020.geojson'))
    data_2020 = pd.read_csv('./resources/Datos_2020_con3_clusters.csv')
    for idx, data in enumerate(data_geo_2020['features']):
        CVEGEO = data['properties']['CVEGEO']
        dataframeRow = data_2020[data_2020['CVEGEO'] == CVEGEO]
        if dataframeRow['CVEGEO'].any():
            data_geo_2020['features'][idx]['properties']['clusters'] = int(dataframeRow['clusters'].values[0])
            data_geo_2020['features'][idx]['properties']['total_hospitales'] = int(dataframeRow['total_hospitales'].values[0])
            data_geo_2020['features'][idx]['properties']['total_consultorios'] = int(dataframeRow['total_consultorios'].values[0])
            data_geo_2020['features'][idx]['properties']['total_enfermeros'] = int(dataframeRow['total_enfermeros'].values[0])
            data_geo_2020['features'][idx]['properties']['total_practicantes_medicos'] = int(dataframeRow['total_practicantes_medicos'].values[0])
            data_geo_2020['features'][idx]['properties']['POBTOT'] = int(dataframeRow['POBTOT'].values[0])
            data_geo_2020['features'][idx]['properties']['POBMAS'] = int(dataframeRow['POBMAS'].values[0])
            data_geo_2020['features'][idx]['properties']['POBFEM'] = int(dataframeRow['POBFEM'].values[0])
            data_geo_2020['features'][idx]['properties']['PSINDER'] = int(dataframeRow['PSINDER'].values[0])
            data_geo_2020['features'][idx]['properties']['PDER_SS'] = int(dataframeRow['PDER_SS'].values[0])
            data_geo_2020['features'][idx]['properties']['VIVTOT'] = int(dataframeRow['VIVTOT'].values[0])
            data_geo_2020['features'][idx]['properties']['VPH_S_ELEC'] = int(dataframeRow['VPH_S_ELEC'].values[0])
            data_geo_2020['features'][idx]['properties']['VPH_AGUAFV'] = int(dataframeRow['VPH_AGUAFV'].values[0])
            data_geo_2020['features'][idx]['properties']['VPH_NODREN'] = int(dataframeRow['VPH_NODREN'].values[0])
    mapa_2020 = folium.Map(tiles='OpenStreetMap', location=[20.838060, -103.602699], zoom_start=10)
    maps = folium.Choropleth(
        geo_data = data_geo_2020,
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
    maps.geojson.add_child(folium.features.GeoJsonTooltip(
        fields=[
            'clusters', 
            'POBTOT',
            'POBMAS',
            'POBFEM',
            'VIVTOT',
            'total_hospitales', 
            'total_consultorios', 
            'total_enfermeros', 
            'total_practicantes_medicos',
            'PSINDER',
            'PDER_SS',
            'VPH_S_ELEC',
            'VPH_AGUAFV',
            'VPH_NODREN'
        ], 
        aliases=[
            'Cluster : ', 
            'Total poblaci??n',
            'Total poblaci??n masculina',
            'Total poblaci??n femenina',
            'Total viviendas',
            'Total hospitales : ', 
            'Total consultorios', 
            'Total enfermeros', 
            'Total practicantes medicos',
            'Total poblaci??n sin afiliaci??n',
            'Total poblaci??n con afiliaci??n',
            'Viviendas sin servicio de energ??a electrica',
            'Viviendas sin servicio de agua potable',
            'Viviendas sin drenaje',
        ], 
        labels=True
    ))   
    folium_static(mapa_2020)
        
def loadData2030() : 
    data_geo_2030 = json.load(open('./resources/AGEBS2030.geojson'))
    data_2030 = pd.read_csv('./resources/Datos_2020_con3_clusters.csv')
    for idx, data in enumerate(data_geo_2030['features']):
        CVEGEO = data['properties']['CVEGEO']
        dataframeRowX = data_2030[data_2030['CVEGEO'] == CVEGEO]
        if dataframeRowX['CVEGEO'].any():
            data_geo_2030['features'][idx]['properties']['clusters'] = int(dataframeRowX['clusters'].values[0])
            data_geo_2030['features'][idx]['properties']['total_hospitales'] = int(dataframeRowX['total_hospitales'].values[0])
            data_geo_2030['features'][idx]['properties']['total_consultorios'] = int(dataframeRowX['total_consultorios'].values[0])
            data_geo_2030['features'][idx]['properties']['total_enfermeros'] = int(dataframeRowX['total_enfermeros'].values[0])
            data_geo_2030['features'][idx]['properties']['total_practicantes_medicos'] = int(dataframeRowX['total_practicantes_medicos'].values[0])
            data_geo_2030['features'][idx]['properties']['POBTOT'] = int(dataframeRowX['POBTOT'].values[0])
            data_geo_2030['features'][idx]['properties']['POBMAS'] = int(dataframeRowX['POBMAS'].values[0])
            data_geo_2030['features'][idx]['properties']['POBFEM'] = int(dataframeRowX['POBFEM'].values[0])
            data_geo_2030['features'][idx]['properties']['PSINDER'] = int(dataframeRowX['PSINDER'].values[0])
            data_geo_2030['features'][idx]['properties']['PDER_SS'] = int(dataframeRowX['PDER_SS'].values[0])
            data_geo_2030['features'][idx]['properties']['VIVTOT'] = int(dataframeRowX['VIVTOT'].values[0])
            data_geo_2030['features'][idx]['properties']['VPH_S_ELEC'] = int(dataframeRowX['VPH_S_ELEC'].values[0])
            data_geo_2030['features'][idx]['properties']['VPH_AGUAFV'] = int(dataframeRowX['VPH_AGUAFV'].values[0])
            data_geo_2030['features'][idx]['properties']['VPH_NODREN'] = int(dataframeRowX['VPH_NODREN'].values[0])
    mapa_2030 = folium.Map(tiles='OpenStreetMap', location=[20.838060, -103.602699], zoom_start=10)
    mapsX = folium.Choropleth(
        geo_data = data_geo_2030,
        data = data_2030,
        columns=['CVEGEO', 'clusters'],
        key_on='feature.properties.CVEGEO',
        fill_color='BuPu', 
        fill_opacity=0.7, 
        line_opacity=0.2,
        highlight=True,
        reset=True
    ).add_to(mapa_2030)
    folium.LayerControl().add_to(mapa_2030)
    tooltip = folium.features.GeoJsonTooltip(
        fields=[
            'clusters', 
            'POBTOT',
            'POBMAS',
            'POBFEM',
            'VIVTOT',
            'total_hospitales', 
            'total_consultorios', 
            'total_enfermeros', 
            'total_practicantes_medicos',
            'PSINDER',
            'PDER_SS',
            'VPH_S_ELEC',
            'VPH_AGUAFV',
            'VPH_NODREN'
        ], 
        aliases=[
            'Cluster : ', 
            'Total poblaci??n',
            'Total poblaci??n masculina',
            'Total poblaci??n femenina',
            'Total viviendas',
            'Total hospitales : ', 
            'Total consultorios', 
            'Total enfermeros', 
            'Total practicantes medicos',
            'Total poblaci??n sin afiliaci??n',
            'Total poblaci??n con afiliaci??n',
            'Viviendas sin servicio de energ??a electrica',
            'Viviendas sin servicio de agua potable',
            'Viviendas sin drenaje',

        ], 
        labels=True
    )
    print(tooltip)
    mapsX.geojson.add_child(tooltip)   
    folium_static(mapa_2030)

col1, col2 = st.columns([1, 11])
with col1:
   st.image("./resources/logo.png")

with col2:
   st.title('Urbalud')



with st.container():
    option = st.selectbox(
    'Selecciona un mapa',
    ('Mapa 2020', 'Mapa 2030'))
    if option == 'Mapa 2020' :
        loadData2020()
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("./resources/2020_cluster1.jpg")
        with col2:
            st.image("./resources/2020_cluster2.jpg")
        with col3:
            st.image("./resources/2020_cluster3.jpg")
    elif option == 'Mapa 2030' :
        loadData2030()
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("./resources/2030_cluster1.jpg")
        with col2:
            st.image("./resources/2030_cluster2.jpg")
        with col3:
            st.image("./resources/2030_cluster3.jpg")

columnsOptions = st.selectbox(
    'Selecciona los datos que quieres comparar entre a??os',
    (
        'Centros medicos', 
        'Personal medico', 
        'Poblaci??n',
        'Viviendas y servicios',
    ))
result = pd.merge(datos_2020, datos_2030, on='CVEGEO', how='outer')
if columnsOptions == 'Centros medicos': 
    st.dataframe(
        data = result.loc[:,['CVEGEO', 'clusters_2020', 'clusters_2030', 'total_hospitales_2020', 'total_hospitales_2030', 'total_consultorios_2020', 'total_consultorios_2030']], 
        height=500
    )
elif columnsOptions == 'Personal medico': 
    st.dataframe(
        data = result.loc[:,['CVEGEO', 'clusters_2020', 'clusters_2030', 'total_medicos_2020', 'total_medicos_2030', 'total_enfermeros_2020', 'total_enfermeros_2030', 'total_practicantes_medicos_2020', 'total_practicantes_medicos_2030']], 
        height=500
    )
elif columnsOptions == 'Poblaci??n': 
    st.dataframe(
        data = result.loc[:,['CVEGEO', 'clusters_2020', 'clusters_2030', 'POBTOT_2020', 'POBTOT_2030', 'POBMAS_2020', 'POBMAS_2030', 'POBFEM_2020', 'POBFEM_2030', 'PSINDER_2020', 'PSINDER_2030']], 
        height=500
    )
elif columnsOptions == 'Viviendas y servicios': 
    st.dataframe(
        data = result.loc[:,['CVEGEO', 'clusters_2020', 'clusters_2030', 'VIVTOT_2020', 'VIVTOT_2030', 'VPH_S_ELEC_2020', 'VPH_S_ELEC_2030', 'VPH_AGUAFV_2020', 'VPH_AGUAFV_2030', 'VPH_NODREN_2020', 'VPH_NODREN_2030']], 
        height=500
    )



