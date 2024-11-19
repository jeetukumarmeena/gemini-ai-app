import json 
import os  
import google.generativeai as genai

# Get the working directory
working_directory = os.path.dirname(os.path.abspath(__file__))

# Path to configuration file
config_file_path = f"{working_directory}/config.json"

# Load configuration data
config_data = json.load(open(config_file_path))

# Load the API key
GOOGLE_API_KEY = config_data["GOOGLE_API_KEY"]

# Configure Google Generative AI with the API key
genai.configure(api_key=GOOGLE_API_KEY)

# Function to load the gemini-1.5-flash model for chatbot
def load_gemini_pro_model():
    gemini_pro_model = genai.GenerationModel("gemini-1.5-flash")
    return gemini_pro_model

# Function for image captioning
def gemini_pro_vision_response(prompt, image):
    gemini_pro_vision_model = genai.GenerativeModel("gemini-1.5-flash")
    response = gemini_pro_vision_model.generate_content([prompt, image])
    result = response.text
    return result

# Function to get the embedding for text
def embedding_model_response(input_text):
    embedding_model = "models/embedding-001"
    embedding = genai.embed_content(model=embedding_model, content=input_text, task_type="retrieval_document")
    embedding_list = embedding["embedding"]
    return embedding

# Function to get the response from gemini-1.5-flash LLM
def gemini_pro_response(user_prompt):
    gemini_pro_model = genai.GenerativeModel("gemini-1.5-flash")
    response = gemini_pro_model.generate_content(user_prompt)
    result = response.text
    return result
