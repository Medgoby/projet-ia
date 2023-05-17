import os, sys
import pandas as pd
import numpy as np
import joblib
import pickle as pkl



def load_model(model_file):
    print(os.path.join(model_file))
    loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
    return loaded_model

# Load Models
def load_model_n_predict(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
    return loaded_model

def etiquetage(value):
    if pd.isna(value):
        return None
    if 'Summer' in value :
        return "Toute l'Afrique"
    if 'Fall' in value :
        return "Afrique Ouest & Afrique Autrale & Afrique Centrale"
    if 'Winter' in value :
        return 'Afrique du Nord'
    if 'Spring' in value :
        return "Toute l'Afrique"
    else:
        return str.lower(value)
    

def astype_cat(df):
    columns=df.select_dtypes(include=['object']).columns.to_list()
    df[columns]=df[columns].astype('category')

def dummies(df):
    data=pd.get_dummies(df)
    return data

def data_process(data):
    data.dropna(inplace=True)
    data=data[data['masterCategory']=="Apparel"]
    data=data[['subCategory','articleType','usage','labels']]
    #data=astype_cat(data)
    # labels_map={"Toute l'Afrique":1,
    #        "Afrique Ouest & Afrique Autrale & Afrique Centrale":2,
    #        "Afrique du Nord":3}
    # data['labels']=data['labels'].map(labels_map)

def split(data):
    from sklearn.model_selection import train_test_split
    X=data.loc[:,data.columns!='labels']
    X.columns=[col.replace(" ","_") for col in X.columns]
    y=data.loc[:,'labels']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    return X_train, X_test, y_train, y_test

def read_data(file):
    df_styles=pd.read_csv(file,sep=';')
    df_styles=df_styles.iloc[:,0:-1]
    df_styles['filename'] = df_styles.apply(lambda row: str(row['id']) + ".jpg", axis=1)



def input_(Apparel_Set,Bottomwear,Dress,Innerwear,Loungewear_and_Nightwear,Saree,Socks,Topwear,Casual,Ethnic,Formal,Party,Smart_Casual,Sports,Travel):
    user_input_dict={
                "Apparel_Set":[Apparel_Set],
                "Bottomwear":[Bottomwear],
                "Dress":[Dress],
                "Innerwear":[Innerwear],
                "Loungewear_and_Nightwear":[Loungewear_and_Nightwear],
                "Saree":[Saree],
                "Socks":[Socks],
                "Topwear":[Topwear],
                "Casual":[Casual],
                "Ethnic":[Ethnic],
                "Formal":[Formal],
                "Party":[Party],
                "Smart_Casual":[Smart_Casual],
                "Sports":[Sports],
                "Travel":[Travel],
            }
    user_input=pd.DataFrame(data=user_input_dict)
    #user_input=np.array(user_input)
    #user_input=user_input.reshape(1,-1)
    #user_input = user_input.replace(cleaner_type)
    return user_input



""" def input_(subCategory,usage):
    user_input_dict={
                'subCategory':[subCategory],
                'usage':[usage],
                            }
    user_input=pd.DataFrame(data=user_input_dict)
    #user_input=np.array(user_input)
    #user_input=user_input.reshape(1,-1)
    cleaner_type = {
                "subCategory":{
                                'Apparel Set':0,
                                'Bottomwear':1,
                                'Dress':2,
                                'Innerwear':3,
                                'Loungewear and Nightwear':4,
                                'Saree':5,
                                'Socks':6,
                                'Topwear':7
                                  },
                "risk_attitude":{
                                'Casual':0, 
                                 'Ethnic':1, 
                                 'Formal':2, 
                                 'Party':3, 
                                 'Smart Casual':4, 
                                 'Sports':5, 
                                 'Travel':6
                                 }
                }
    user_input = user_input.replace(cleaner_type)
    return user_input """
