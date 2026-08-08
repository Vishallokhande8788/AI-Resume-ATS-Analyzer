from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

import streamlit as st
import os
from PIL import Image
import pdf2image
import google.generativeai as genai 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) 

def get_gemini_response(input,pdf_content,prompt):
    model = genai.