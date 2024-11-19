# gemini_utility.py
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

# function to load the gemini-pro model for chatbot
def load_gemini_pro_model():
    gemini_pro_model = genai.GenerationModel("gemini-pro")
    return gemini_pro_model

# function for image captioning

def gemini_pro_vision_response(promt,image):
    gemini_pro_vision_model = genai.GenerativeModel("gemini-pro-vision")
    response = gemini_pro_vision_model.generate_content([promt,image ])
    result =response.text
    return result




# function to get the embedding for text

def embedding_model_response(input_text):
    embedding_model = "models/embeddinh-001"
    embedding = genai.embed_content(model= embedding_model,content=input_text, task_type="retrieval_document")
    embedding_list = embedding["embedding"]
    return embedding


# function to get the response form gemini-pro LLM
def gemini_pro_response(user_promt):
    gemini_pro_model = genai.GenerativeModel("gemini-pro")
    response = gemini_pro_model.generate_content(user_promt)
    result = response.text
    return result

output = gemini_pro_response("what is machine learning")
print (output)