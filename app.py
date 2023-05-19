import os, sys
import pandas as pd 
import numpy as np 
import streamlit as st
import streamlit.components.v1 as stc 
import joblib
import pickle as pkl
from pathlib import Path
from PIL import Image
import scikitplot as skplt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
#from sklearn.metrics import plot_confusion_matrix, plot_roc_curve, plot_precision_recall_curve

from streamlit_yellowbrick import st_yellowbrick
from yellowbrick.classifier import ClassificationReport
from yellowbrick.classifier import ConfusionMatrix
from yellowbrick.classifier import ClassPredictionError
from yellowbrick.model_selection import FeatureImportances


import matplotlib.pyplot as plt
import folium
from streamlit_folium import st_folium, folium_static

# path=Path.cwd().parent
# os.chdir(path)

from features_engineering.utils import load_model
from features_engineering.utils import input_

import plotly.express as px
import plotly.graph_objects as go

import streamlit as st
from streamlit_option_menu import option_menu
st.set_option('deprecation.showPyplotGlobalUse', False)

#data['labels']=data['season'].apply(lambda x: etiquetage(x))

#st.set_page_config(layout="wide")
st.set_page_config(
    page_title="Fast fashion",
    page_icon="🌍",layout="wide")

#@st.cache_resource

#from features_engineering.utils import*


# DIRPATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# os.chdir(DIRPATH)


#model = utils.load_model("./models/rf_model.pkl")



#st.write(pd.read_csv("./data/styles.csv",sep=';'))

#st.write(read_data("./data/styles.csv"))

#read_data("./data/styles.csv")



def main():
    model =load_model("./models/rf_model.pkl")

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
            st.markdown("""<h2 style='text-align: center;width:100% ;margin-left:-0%;padding: 0px 0px 0px 0px;color: #1699de;'>Image d'une decharge au Ghana</h>""", unsafe_allow_html=True)
            st.image("https://www.leparisien.fr/resizer/NaGTvnYH3tCp1H5nW85oqHt8yV0=/arc-anglerfish-eu-central-1-prod-leparisien/public/4IFWKW45BNDVZNQPSENOHWQXCQ.jpg",
                    caption='Une decharge au Ghana')
            
        with col2:
            st.markdown("""<h2 style='text-align: center;width:100% ;margin-left:-0%;padding: 0px 0px 0px 0px;color: #1699de;'>Carte D'Afrique</h>""", unsafe_allow_html=True)
            image = Image.open('./images/afrique.png')
            st.image(image, caption="Les pays d'Afrique")            

    if choose=="Make Prediction":

        model =load_model("./models/rf_model.pkl")
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

        user_input=input_(Apparel_Set,Bottomwear,Dress,Innerwear,Loungewear_and_Nightwear,Saree,Socks,Topwear,Casual,Ethnic,Formal,Party,Smart_Casual,Sports,Travel)
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

        X=pd.read_csv("./data/X.csv",index_col=0)
        y=pd.read_csv("./data/y.csv",index_col=0)

        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

        # skplt.metrics.plot_confusion_matrix(y_test, model.predict(X_test), normalize=True)
        # #plt.figure(figsize=(8,8))
        # plt.show()
        # st.pyplot()

        # from sklearn.metrics import classification_report
        # classification_report(y_test, model.predict(X_test))

        #classes = ["Toute l'Afrique", "Afrique Ouest & Afrique Autrale & Afrique Centrale","Afrique du Nord"]
        #classes = [1,2,3]

        col1,col2=st.columns([2,2])
        with col1:
            #st.subheader("Classification Report Metrics")
            st.markdown("""<h2 style='text-align: center;width:100% ;margin-left:-0%;padding: 0px 0px 0px 0px;color: #1699de;'>Classification Report Metrics</h>""", unsafe_allow_html=True)
            vizualizer = ClassificationReport(model, support=True)
            vizualizer.fit(X_train, y_train)
            vizualizer.score(X_test, y_test)
            st_yellowbrick(vizualizer)

        with col2:
            #st.subheader("Features Importances")
            st.markdown("""<h2 style='text-align: center;width:100% ;margin-left:-0%;padding: 0px 0px 0px 0px;color: #1699de;'>Features Importances</h>""", unsafe_allow_html=True)
            visualizer = FeatureImportances(model)
            visualizer.fit(X_train, y_train)
            st_yellowbrick(visualizer)
            #visualizer.show();

        #st.subheader("Confusion Matrix")
        st.markdown("""<h2 style='text-align: center;width:100% ;margin-left:-0%;padding: 0px 0px 0px 0px;color: #1699de;'>Confusion Matrix</h>""", unsafe_allow_html=True)
        cm = ConfusionMatrix(
                model,
                percent=True
                #label_encoder={0: 'Adelie', 1: 'Chinstrap', 2: 'Gentoo'}
            )
        cm.fit(X_train, y_train)
        cm.score(X_test, y_test)
        st_yellowbrick(cm)
            

        


        # visualizer = ClassPredictionError(
        #     model)
        # visualizer.fit(X_train, y_train)
        # visualizer.score(X_test, y_test)
        # st_yellowbrick(visualizer)


       
        # st.write(X_train)
        # st.write(y_train)

        


        
if __name__ == '__main__':
	main()



