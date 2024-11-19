import streamlit as st
from streamlit_option_menu import option_menu
import os

# get the working directory
working_directory = os.path.dirname(os.path.abspath(__file__))


    
#setting up the page configuration

st.set_page_config(
    page_title="Gemini_AI",
    page_icon="🧠",
    layout="centered"
)

with st.sidebar:
    selected = option_menu("Gemini AI", ["Chatbot", "Image Captioning", "Embed Text", "Ask me Anything"], menu_icon='robot', icons=['chat-dot-fill', 'image-fill', 'textarea-t', 'patch-question-fill'],default_index =0)
