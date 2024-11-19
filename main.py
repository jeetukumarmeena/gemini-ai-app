import streamlit as st
from streamlit_option_menu import option_menu
import os
from gemini_utility import (load_gemini_pro_model,
                            gemini_pro_vision_response,
                            embedding_model_response,
                            gemini_pro_response)
from PIL import Image

# Get the working directory
working_directory = os.path.dirname(os.path.abspath(__file__))

# Setting up the page configuration
st.set_page_config(
    page_title="Gemini_AI",
    page_icon="🧠",
    layout="centered"
)

with st.sidebar:
    selected = option_menu("Gemini AI",
                           ["ChatBot", "Image Captioning", "Embed Text", "Ask me Anything"], 
                           menu_icon='robot', 
                           icons=['chat-dot-fill', 'image-fill', 'textarea-t', 'patch-question-fill'], 
                           default_index=0)

# Function to translate role between Gemini-pro and Streamlit technology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

if selected == "ChatBot":
    model = load_gemini_pro_model()

    # Initialize chat session in Streamlit if not already present
    if "chat_session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])
    
    # Streamlit page title
    st.title("🤖 ChatBot")
    
    # Display chat history
    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)

    # Input field for user message 
    user_prompt = st.chat_input("Ask Me Jeetu pro...")
    if user_prompt:
        st.chat_message("user").markdown(user_prompt)
        gemini_response = st.session_state.chat_session.send_message(user_prompt)

        # Display Gemini-pro response
        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)

# Image captioning page
if selected == "Image Captioning":
    # Streamlit page title
    st.title(" 📷 Snap Narrate")
    uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])
    if st.button("Generate Caption"):
        image = Image.open(uploaded_image)
        col1, col2 = st.columns(2)
        with col1:
            resized_image = image.resize((800, 500))
            st.image(resized_image)
        default_prompt = "write a short caption for this image"
        caption = gemini_pro_vision_response(default_prompt, image)

        with col2:
            st.info(caption)

# Text embedding page
if selected == "Embed Text":
    st.title("🔠 Embed Text")
    # Input text box
    input_text = st.text_area(label="", placeholder="Enter the text to embed")
    if st.button("Get Embeddings"):
        response = embedding_model_response(input_text)
        st.markdown(response)

# Question answering page
if selected == "Ask me Anything":
    st.title("❓ Ask me a question")
    # Text box to enter prompt
    user_prompt = st.text_area(label="", placeholder="Ask Gemini pro...")
    if st.button("Get an answer"):
        response = gemini_pro_response(user_prompt)
        st.markdown(response)
