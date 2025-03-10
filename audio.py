import streamlit as st
import requests
import io
import base64
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get API keys from environment variables
subscription_key = os.getenv("SARVAM_SUBSCRIPTION_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

# Define the LLM model (if using OpenAI)
LLM = "text-davinci-003"  # Example model, adjust as needed

# Initialize OpenAI client (if using OpenAI)
if openai_api_key:
    import openai
    openai.api_key = openai_api_key
else:
    st.error("OpenAI API Key not found in environment variables.")

sarvamurl = "https://api.sarvam.ai/text-to-speech"
sarvamheaders = {
    "accept": "application/json",
    "content-type": "application/json",
    "api-subscription-key": subscription_key
}

# Function to send audio to Sarvam API for speech recognition
def transcribe_audio(audio_file, subscription_key, language_code='hi-IN'):
    url = "https://api.sarvam.ai/speech-to-text"
    payload = {
        'model': 'saarika:v2',
        'language_code': language_code,
        'with_timesteps': 'false'
    }
    files = [
        ('file', ('audio.wav', audio_file, 'audio/wav'))
    ]
    headers = {
        'api-subscription-key': subscription_key
    }
    response = requests.post(url, headers=headers, data=payload, files=files)
    if response.status_code == 200:
        return response.json().get('transcript', 'No transcript available.')
    else:
        return f"Error: {response.status_code}, {response.text}"

# Function to process text using OpenAI API
def process_with_llm(text):
    try:
        response = openai.Completion.create(
            model=LLM,
            prompt=text,
            max_tokens=100
        )
        return response.choices[0].text
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Language code mapping
language_mapping = {
    "English":"en-IN",
    "Hindi": "hi-IN",
    "Bengali": "bn-IN",
    "Kannada": "kn-IN",
    "Malayalam": "ml-IN",
    "Marathi": "mr-IN",
    "Odia": "od-IN",
    "Punjabi": "pa-IN",
    "Tamil": "ta-IN",
    "Telugu": "te-IN",
    "Gujarati": "gu-IN"
}

# Streamlit UI
st.title("Ashvin the Smart AI Therapist")
with st.sidebar:
    selected_language = st.selectbox("Select Language:", 
                                  list(language_mapping.keys()), 
                                  index=0)
    language_code = language_mapping[selected_language]

audio_value = st.audio_input("Record a voice message")
if audio_value:
    if subscription_key:
        with st.spinner("Transcribing..."):
            transcript = transcribe_audio(audio_value, subscription_key, language_code)
            st.write(f"User: {transcript}")
            # Process the transcript with OpenAI
            if openai_api_key:
                with st.spinner("Processing with Model..."):
                    model_response = process_with_llm(transcript)
