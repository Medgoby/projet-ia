import os, sys
import pandas as pd 
import numpy as np 
import streamlit as st
import streamlit.components.v1 as stc 
import joblib
import pickle as pkl
from pathlib import Path

import folium
from streamlit_folium import st_folium, folium_static

path=Path.cwd().parent
os.chdir(path)

from features_engineering import utils

import plotly.express as px
import plotly.graph_objects as go

#data['labels']=data['season'].apply(lambda x: etiquetage(x))

st.set_page_config(layout="wide")



def main():

    html_temp = """ 
            <div style ="background-color:#1699de;padding:13px"> 
            <h1 style ="color:white;text-align:center;">Application de seconde main à destination des pays d'Afrique</h1> 
            </div> 
            """
    stc.html(html_temp)

if __name__ == '__main__':
	main()


{'Apparel Set','Bottomwear','Dress','Innerwear','Loungewear and Nightwear','Saree','Socks','Topwear'}


#model = load_model("./models/xgb_model.pkl")

{'Casual', 'Ethnic', 'Formal', 'Party', 'Smart Casual', 'Sports', 'Travel'}

with st.sidebar.expander("➕ &nbsp; Variable choice", expanded=False):
    #source_type = st.radio("Variable", ["subCategory", "usual"], label_visibility="collapsed")

    with st.form("input_form"):
        #if source_type == "subCategory":
        Apparel=st.sidebar.selectbox("Apparel",(False,True))
        Bottomwear=st.sidebar.selectbox("Bottomwear",(False,True))
        Dress=st.sidebar.selectbox("Dress",(False,True))
        Innerwear=st.sidebar.selectbox("Innerwear",(False,True))
        Loungewear_Nightwear=st.sidebar.selectbox("Loungewear and Nightwear",(False,True))
        Saree=st.sidebar.selectbox("Saree",(False,True))
        Socks=st.sidebar.selectbox("Socks",(False,True))
        Topwear=st.sidebar.selectbox("Topwear",(False,True))

        #elif source_type == "usual":
        Casual=st.sidebar.selectbox("Casual",(False,True))
        Ethnic=st.sidebar.selectbox("Ethnic",(False,True))
        Formal=st.sidebar.selectbox("Formal",(False,True))
        Party=st.sidebar.selectbox("Party",(False,True))
        Smart_Casual=st.sidebar.selectbox("Smart Casual",(False,True))
        Sports=st.sidebar.selectbox("Sports",(False,True))
        Travel=st.sidebar.selectbox("Travel",(False,True))
        subCategory = st.form_submit_button(label="subCategory")

                                                        
""" subCategory=st.sidebar.selectbox("Article SubCategory",('Apparel Set',
                                  'Bottomwear',
                                  'Dress',
                                  'Innerwear',
                                  'Loungewear and Nightwear',
                                  'Saree',
                                  'Socks',
                                  'Topwear'
                                  )
            )

usage=st.sidebar.selectbox("Usage",('Casual', 'Ethnic', 'Formal', 'Party', 'Smart Casual', 'Sports', 'Travel'
                                  )
            )
 """

user_input=utils.input_(Apparel,Bottomwear,Dress,Innerwear,Loungewear_Nightwear,Saree,Socks,Topwear,Casual,Ethnic,Formal,Party,Smart_Casual,Sports,Travel)
#user_input=utils.dummies(user_input)
#user_input=(subCategory,usage,articleType)
st.write(user_input)



# with st.sidebar.expander("➕Add Media", expanded=False):
#     Category=st.selectbox("Category",('Apparel Set',
#                                   'Bottomwear',
#                                   'Dress',
#                                   'Innerwear',
#                                   'Loungewear and Nightwear',
#                                   'Saree',
#                                   'Socks',
#                                   'Topwear'
#                                   )
#             )

# with st.sidebar.expander("subCategory", expanded=False):
#     subCategory=st.selectbox("subCategory",('Casual', 'Ethnic', 'Formal', 'Party', 'Smart Casual', 'Sports', 'Travel'
#                                     )
#                 )
    
# with st.sidebar.expander("Type", expanded=False):
#     Type=st.selectbox("Type",('Baby Dolls','Bath Robe','Belts','Blazers','Booties','Boxers','Bra','Briefs','Camisoles','Capris',
#                                 'Churidar','Clothing Set','Dresses','Dupatta','Innerwear Vests','Jackets','Jeans','Jeggings',
#                                 'Jumpsuit','Kurta Sets','Kurtas','Kurtis','Leggings','Lehenga Choli','Lounge Pants','Lounge Shorts',
#                                 'Lounge Tshirts','Nehru Jackets','Night suits','Nightdress','Patiala','Rain Jacket','Robe',
#                                 'Rompers','Salwar','Salwar and Dupatta','Sarees','Shapewear','Shirts','Shorts','Shrug','Skirts',
#                                 'Stockings','Suits','Suspenders','Sweaters','Sweatshirts','Swimwear','Tights','Tops','Track Pants',
#                                 'Tracksuits','Trousers','Trunk','Tshirts','Tunics','Waistcoat'
#                         )
#                 )

        


world_map= folium.Map(tiles="cartodbpositron")
#st.map(world_map)

# center on Liberty Bell, add marker
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
folium.Marker(
    [-8.783195, 34.50852299999997], popup="Liberty Bell", tooltip="Liberty Bell"
).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)




