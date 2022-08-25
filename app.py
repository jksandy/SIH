import streamlit.components.v1 as components
import streamlit as st
import pandas as pd
import os
from PIL import Image
import numpy as np
import hydralit_components as hc
import bgfg
import stt
import time
import key
import map

def del_files():
  directory = "./seperated"
  files_in_directory = os.listdir(directory)
  filtered_files = [file for file in files_in_directory if file.endswith(".wav")]
  for file in filtered_files:
    path_to_file = os.path.join(directory, file)
    os.remove(path_to_file)
  filtered_files = [file for file in files_in_directory if file.endswith(".mp3")]
  for file in filtered_files:
    path_to_file = os.path.join(directory, file)
    os.remove(path_to_file)

parent_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(parent_dir, "st_audiorec/frontend/build")
st_audiorec = components.declare_component("st_audiorec", path=build_dir)
bf = 0

st.set_page_config(page_title = "Kaaval AI", page_icon = "⭐", layout="wide")

image2 = Image.open('img/flag.png')  

menu_data = [
        {'id': 'aud','icon': "fas fa-volume-up", 'label':"Audio Processor"},
        {'id':'pred','icon':"fas fa-user-shield",'label':"Crime Forecast"},
        {'id':'vis', 'icon': "far fa-chart-bar", 'label':"Charts"},
        {'id':'rep', 'icon': "far fa-eye", 'label':"Report a Crime"},
]
over_theme = {'txc_inactive': '#FFFFFF'}
menu_id = hc.nav_bar(menu_definition=menu_data,home_name='Home',override_theme=over_theme, sticky_mode = 'sticky')
st.write("\n")


setval = 0
def on():
  global setval 
  setval = 1

if menu_id == 'Home':
  del_files()
  imco = st.columns([0.16,1,0.23])
  with imco[0]:
    logo = Image.open('img/Logo.png')
    st.image(logo, width = 150)
  with imco[1]:
    st.write("\n")
    st.title("⭐Kaaval AI")
    st.subheader("A Portal for the Simulation of the AI based PCR")
    st.text(" \n")
  with imco[2]:
    st.text("\n")
    flag = Image.open('img/flag.png')
    st.image(flag, width = 200)
  image1 = Image.open('img/police.jpg')
  st.image(image1)
  st.write("\n\n")
  theme1 = {'bgcolor': '#ffffff','title_color': '#072F5F','content_color': '#072F5F' }
  ff = st.columns(1)
  aa = st.columns(3)
  st.write("\n")
  st.write("\n")
  with aa[1]:
    st.title('Features of the System')
  cc = st.columns(4)
  with cc[0]:
    hc.info_card(title='Audio Processing', content='Even the Background noises aren\'t ignored!', theme_override= theme1,bar_value=0)
  with cc[1]:
    hc.info_card(title='Crime Forecasting', content='Prediction of Law and Order Events with Location and Time', theme_override= theme1,bar_value=0)
  with cc[2]:
    hc.info_card(title='Spatial Visualisation', content='Plots of Crime data over a map', theme_override= theme1,bar_value=0)
  with cc[3]:  
    hc.info_card(title='Temporal Visualisation', content='Chronology of Crime events', theme_override= theme1,bar_value=0)
  
elif menu_id == 'aud':
  del_files()
  st.title("Audio Processing:")
  st.text("Either use the File Uploader or make use of the recorder to get an Audio sample and then upload:")
  recorder, upload = st.tabs(["Audio Recorder", "File Uploader"])
  with recorder:
    st.write("Audio Recorder")
    st_audiorec()
  with upload:
    st.write("File Uploader")
    uploaded_file = st.file_uploader("Choose a Audio file to Process:")
  st.write("\n")
  st.write("\n")
  st.write("\n")
  if uploaded_file is not None:
    audio_bytes = uploaded_file.read()
    with open(os.path.join("media/file.wav"), "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.error("File Uploaded")
    st.audio("media/file.wav", format="audio/mp3")
  #   on() 
  # if(setval == 1):
  #   st.title("Background - Foreground separation of the Audio")
  #   st.text("BACKGROUND gives inferences of the possible event happening around!")
  #   st.text("FOREGROUND has the Speech component!")
  #   a = st.button("SEPERATE")
  #   if(a):
  #     a = 1
  #     if bgfg.seperate() == 1:
  #       st.title("Background Audio: ")
  #       st.audio("seperated/mp3/background_signal.wav", format="audio/wav")
  #       st.text("\n")
  #       st.title("Foreground Audio: ")
  #       st.audio("seperated/mp3/foreground_signal.wav", format="audio/wav")       
    st.title("Speech converted to Text")
    co = st.columns(3)
    with co[0]:
      option = st.selectbox("Language of the Audio: ",["English", "Hindi"])
    tb = st.button("TRANSCRIBE")
    while(tb):
      a = 1
      stt.print_text(option)
      st.header("Transcribed Text")
      st.write(stt.text)
      st.title("Extraction of Keywords from Text")
      st.text("\n")
      st.button("Get Keywords")
      if():
        key.vectorize(stt.text)


elif menu_id == 'pred':
  st.title("Crime data collected from News articles to simulate the PCR environment")
  datadf = pd.read_csv("SIH Data.csv")
  datanew = pd.DataFrame(datadf[~datadf['Article'].isnull()])
  datanew.index = np.arange(1, len(datanew)+1)
  st.dataframe(datanew, 2000, 2000)

elif menu_id == 'vis':
  del_files()
  st.title("Visualizing Crime distribution Spatially")
  st.write("Mapping Crime to the Cities...")
  map.spatio()
  st.title("Crime Plots")
  vis = st.columns(2)
  with vis[0]:
    map.stats()
  st.title("Visualising Crime data Temporally")

elif menu_id == 'rep':
  with st.form("crime_form"):
    banner = Image.open("img/banner.jpg")
    st.image(banner, use_column_width=True)
    st.header("Fill out Form to report crimes")
    loc = st.text_input("Crime Location")
    cr = st.text_area("Crime Description")
    dat = st.date_input("Date")
    tc = st.time_input("Time of Crime")
    st.text("Either use the File Uploader or make use of the recorder to get an Audio sample and then upload:")
    recorder, upload, live = st.tabs(["Audio Recorder", "File Uploader", "Live Audio"])
    with recorder:
      st.write("Audio Recorder")
      st_audiorec()
    with upload:
      st.write("File Uploader")   
      uploaded_file = st.file_uploader("Choose a Audio file to Process:")
    with live:
      rec = st.button("Record")
      stop = st.button("Stop")
    done = st.form_submit_button("Submit")