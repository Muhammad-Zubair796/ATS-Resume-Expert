from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
from PIL import Image
import pdf2image
import google.generativeai as genai

# Configure Google Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from Gemini model
def get_gemini_response(input_text, pdf_image, prompt):
    # Using the official, current multimodal model
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    # The new SDK allows us to pass the PIL Image directly! No base64 needed.
    response = model.generate_content([input_text, pdf_image, prompt])
    return response.text

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