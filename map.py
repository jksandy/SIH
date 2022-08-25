import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pydeck as pdk



def spatio():
    data = pd.read_csv("SIH Data.csv")
    data = data[data["Article"].notna()]
    data = data[["Latitude","Longitude","Crime"]]
    newdf = pd.DataFrame(columns=["latitude","longitude", "Crime"])
    newdf["latitude"], newdf["longitude"], newdf["Crime"] = data["Latitude"], data["Longitude"], data["Crime"]
    newdf["latitude"].astype(float)
    newdf["longitude"].astype(float)
    print(len(newdf))
    st.pydeck_chart(pdk.Deck(
     map_style='road',
     initial_view_state=pdk.ViewState(
         latitude=28.66,
         longitude=77.2,
         zoom=9,
     ),
     layers=[
         pdk.Layer(
             'ScatterplotLayer',
             data=newdf,
             get_position='[longitude, latitude]',
             get_color='[200, 30, 0, 160]',
             get_radius=700,
         ),
         pdk.Layer(
            "TextLayer",
            data = newdf,
            get_position='[longitude, latitude]',
            get_text="Crime",
            get_size=17,
         )
     ],
 ))


def temporal():
    data = pd.read_csv("SIH Data.csv")
    data = data[data["Article"].notna()]
    

def stats():
    data = pd.read_csv("SIH Data.csv")
    data = data[data["Article"].notna()]
    count = data["Crime"].value_counts()
    fig = plt.figure(figsize=(5,3))
    ax= plt.axes()
    ax.pie(count.values, labels=count.index,textprops={'fontsize': 4}, startangle=250)
    st.pyplot(fig)  