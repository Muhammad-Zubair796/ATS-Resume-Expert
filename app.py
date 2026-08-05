from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
from PIL import Image
import pdf2image
import google.generativeai as genai

# Configure Google Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from Gemini model with Ultimate Fallback
def get_gemini_response(input_text, pdf_image, prompt):
    # A list of every possible valid Google model that supports images
    models_to_try = [
        "gemini-1.5-flash",
        "gemini-1.5-flash-001",
        "gemini-1.5-flash-002",
        "gemini-1.5-pro",
        "gemini-1.0-pro-vision-latest"
    ]
    
    last_error = None
    
    # Try each model one by one until Google accepts one
    for model_name in models_to_try:
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content([input_text, pdf_image, prompt])
            return response.text
        except Exception as e:
            print(f"Model {model_name} failed. Trying next... Error: {e}")
            last_error = e
            continue # Go to the next model in the list
            
    # If ALL models fail, show the error on the screen so we know exactly why
    return f"Error: Google API rejected all models. Last error: {last_error}"

# Function to convert PDF to a PIL Image
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Convert PDF to images
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        # Return the first page as a standard PIL Image
        first_page = images[0]
        return first_page
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit App
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")

# User input
input_text = st.text_area("Job Description:", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.write("✅ PDF Uploaded Successfully")

# Buttons
submit1 = st.button("Tell Me About the Resume")
submit3 = st.button("Percentage Match")

# Prompts for AI
input_prompt1 = """
You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description.
Please share your professional evaluation on whether the candidate's profile aligns with the role.
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality.
Your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches
the job description. First, the output should come as percentage, then keywords missing, and finally the final thoughts.
"""

# Handle button actions
if submit1:
    if uploaded_file is not None:
        with st.spinner("Analyzing resume... Please wait."):
            pdf_image = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_text, pdf_image, input_prompt1)
            st.subheader("The Response is")
            st.write(response)
    else:
        st.error("Please upload the resume")

elif submit3:
    if uploaded_file is not None:
        with st.spinner("Calculating match percentage... Please wait."):
            pdf_image = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_text, pdf_image, input_prompt3)
            st.subheader("The Response is")
            st.write(response)
    else:
        st.error("Please upload the resume")

# Footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 10px;
        right: 10px;
        font-size: 14px;
        color: grey;
    }
    </style>
    <div class="footer">
        👨‍💻 Developed by <b>Muhammad Zubair</b>
    </div>
    """,
    unsafe_allow_html=True
)