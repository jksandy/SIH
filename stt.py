import os
from os import path
from pydub import AudioSegment
import streamlit as st
aud = "media/file.wav"
from pydub.utils import make_chunks 
import speech_recognition as sr
from googletrans import Translator 


i = 0
text = ""

def chunk_audio():
    myaudio = AudioSegment.from_file(aud, "wav") 
    global i
    chunk_length_ms = 8000 # pydub calculates in millisec 
    chunks = make_chunks(myaudio,chunk_length_ms) #Make chunks of one sec 
    for i, chunk in enumerate(chunks): 
        chunk_name = "chunks/{0}.wav".format(i) 
        print ("exporting", chunk_name) 
        chunk.export(chunk_name, format="wav") 

def print_text(language):
    lan = ""
    if(language == "English"):
        lan = "en-US"
    else:
        lan = "hi-IN" 
    chunk_audio()
    r = sr.Recognizer()
    global text, i
    text = ""
    for j in range(i + 1):
        file="chunks/{0}.wav".format(j)
        print("Translating",j)
        with sr.AudioFile(file) as source:
            audio = r.listen(source)
        text = text + "\n" + r.recognize_google(audio, language=lan)
        if(language == "Hindi"):
            translator = Translator()  
            translate_text = translator.translate(text,src="hi",dest="en")  
            st.write(translate_text.text)