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

import streamlit as st
from streamlit_option_menu import option_menu

#data['labels']=data['season'].apply(lambda x: etiquetage(x))

#st.set_page_config(layout="wide")
st.set_page_config(
    page_title="Fast fashion",
    page_icon="🌍",layout="wide")

#@st.cache_resource



DIRPATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
os.chdir(DIRPATH)


#model = utils.load_model("./models/rf_model.pkl")




def main():

    html_temp = """ 
            <div style ="background-color:#1699de;padding:13px"> 
            <h1 style ="color:white;text-align:center;">Application de seconde main à destination des pays d'Afrique</h1> 
            </div> 
            """
    stc.html(html_temp)

    with st.sidebar:
        choose = option_menu("APP 🌍", ["Home", "Make Prediction"],
                            icons=['house', 'clipboard-data'],
                            #menu_icon="app-indicator", 
                            menu_icon="cast",
                            default_index=0,
                            styles={
                                    "container": {"padding": "5!important", "background-color": "#fafafa"},
                                    "icon": {"color": "black", "font-size": "25px"}, 
                                    "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                                    "nav-link-selected": {"background-color": "#1699de"},
                                }
                            )
        
    if choose=="Home":
        col1,col2=st.columns(2)

        with col1:
         st.image("https://www.leparisien.fr/resizer/NaGTvnYH3tCp1H5nW85oqHt8yV0=/arc-anglerfish-eu-central-1-prod-leparisien/public/4IFWKW45BNDVZNQPSENOHWQXCQ.jpg",
                    caption='Une decharge au Ghana')
            
        with col2:
            # center on Liberty Bell, add marker
            m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
            folium.Marker(
                [-8.783195, 34.50852299999997], popup="Liberty Bell", tooltip="Liberty Bell"
            ).add_to(m)

            # call to render Folium map in Streamlit
            st_data = st_folium(m, width=725)
            

    if choose=="Make Prediction":

        model = utils.load_model("./models/rf_model.pkl")
        #model = load_model("./models/rf_model.pkl")

        with st.sidebar.expander("➕ &nbsp; Variable choice", expanded=False):
            #source_type = st.radio("Variable", ["subCategory", "usual"], label_visibility="collapsed")

            with st.form("input_form"):
                #if source_type == "subCategory":
                Apparel_Set=st.sidebar.selectbox("Apparel",(False,True))
                Bottomwear=st.sidebar.selectbox("Bottomwear",(False,True))
                Dress=st.sidebar.selectbox("Dress",(False,True))
                Innerwear=st.sidebar.selectbox("Innerwear",(False,True))
                Loungewear_and_Nightwear=st.sidebar.selectbox("Loungewear and Nightwear",(False,True))
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
                #subCategory = st.form_submit_button(label="subCategory")

        user_input=utils.input_(Apparel_Set,Bottomwear,Dress,Innerwear,Loungewear_and_Nightwear,Saree,Socks,Topwear,Casual,Ethnic,Formal,Party,Smart_Casual,Sports,Travel)
        #user_input=utils.dummies(user_input)
        #user_input=(subCategory,usage,articleType)
        st.write(user_input)

        btn_predict = st.button("Predict")

        if btn_predict:
            pred = model.predict(user_input)
            if pred==1:
                st.success("Ce type de vêtement peut être distribué dans tous les pays d'Afrique",icon="✅")
            if pred==2:
                st.warning("Ce type de vêtement peut être distribué en Afrique Ouest & Afrique Autrale & Afrique Centrale",icon="🚨")    
            if pred==3:
                st.warning("Ce type de vêtement peut être distribué en Afrique du Nord",icon="🚨")


        
if __name__ == '__main__':
	main()



#world_map= folium.Map(tiles="cartodbpositron")
#st.map(world_map)


# with st.sidebar:
#     selected = option_menu("Main Menu", ["Home", 'Classification'], 
#         icons=['house', 'clipboard-data'], menu_icon="cast", default_index=1)
#     selected



#{'Apparel Set','Bottomwear','Dress','Innerwear','Loungewear and Nightwear','Saree','Socks','Topwear'}


#model = load_model("./models/xgb_model.pkl")

#{'Casual', 'Ethnic', 'Formal', 'Party', 'Smart Casual', 'Sports', 'Travel'}

# with st.sidebar.expander("➕ &nbsp; Variable choice", expanded=False):
#     #source_type = st.radio("Variable", ["subCategory", "usual"], label_visibility="collapsed")

#     with st.form("input_form"):
#         #if source_type == "subCategory":
#         Apparel=st.sidebar.selectbox("Apparel",(False,True))
#         Bottomwear=st.sidebar.selectbox("Bottomwear",(False,True))
#         Dress=st.sidebar.selectbox("Dress",(False,True))
#         Innerwear=st.sidebar.selectbox("Innerwear",(False,True))
#         Loungewear_Nightwear=st.sidebar.selectbox("Loungewear and Nightwear",(False,True))
#         Saree=st.sidebar.selectbox("Saree",(False,True))
#         Socks=st.sidebar.selectbox("Socks",(False,True))
#         Topwear=st.sidebar.selectbox("Topwear",(False,True))

#         #elif source_type == "usual":
#         Casual=st.sidebar.selectbox("Casual",(False,True))
#         Ethnic=st.sidebar.selectbox("Ethnic",(False,True))
#         Formal=st.sidebar.selectbox("Formal",(False,True))
#         Party=st.sidebar.selectbox("Party",(False,True))
#         Smart_Casual=st.sidebar.selectbox("Smart Casual",(False,True))
#         Sports=st.sidebar.selectbox("Sports",(False,True))
#         Travel=st.sidebar.selectbox("Travel",(False,True))
#         subCategory = st.form_submit_button(label="subCategory")

# user_input=utils.input_(Apparel,Bottomwear,Dress,Innerwear,Loungewear_Nightwear,Saree,Socks,Topwear,Casual,Ethnic,Formal,Party,Smart_Casual,Sports,Travel)
# #user_input=utils.dummies(user_input)
# #user_input=(subCategory,usage,articleType)
# st.write(user_input)



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

        















