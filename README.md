# 📄 ATS Resume Expert - AI Powered Resume Analyzer

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Click%20Here-success?style=for-the-badge)](https://ats-resume-expert-1.onrender.com)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white)
![Open Source](https://img.shields.io/badge/Open%20Source-Yes-success?style=for-the-badge)

**ATS Resume Expert** is a powerful, AI-driven Applicant Tracking System (ATS) built with Python and Streamlit. It leverages the latest **Google Gemini Flash** models to evaluate resumes (PDFs) against specific Job Descriptions, providing HR-level insights and ATS match percentages.

🌐 **Try it live here:** [https://ats-resume-expert-1.onrender.com](https://ats-resume-expert-1.onrender.com)

---

## 🚀 Features

- **👨‍💼 HR Manager Evaluation:** Get a professional review of the candidate's profile, highlighting strengths and weaknesses based on the job requirements.
- **📊 ATS Percentage Match:** Calculates the exact percentage match between the resume and the job description.
- **🔑 Keyword Analysis:** Identifies missing keywords that the candidate should add to improve their ATS score.
- **📄 PDF Processing:** Seamlessly converts uploaded PDF resumes into processable data using `pdf2image`.

---

## 🛠️ Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **AI Model:** [Google Generative AI (Gemini Flash Latest)](https://ai.google.dev/)
- **PDF Processing:** `pdf2image`, `Pillow`
- **Environment Management:** `python-dotenv`
- **Cloud Hosting:** [Render](https://render.com/)

---

## ⚙️ Prerequisites

Before running this application locally, you must install **Poppler**, which is required by the `pdf2image` library to read PDF files.

- **Windows:** Download Poppler from [here](https://github.com/oschwartz10612/poppler-windows/releases/), extract it, and add the `bin` folder to your system's PATH environment variable.
- **Mac:** Run `brew install poppler`
- **Linux:** Run `sudo apt-get install poppler-utils`

---

## 💻 Installation & Setup

Follow these steps to run the project locally on your machine.

**1. Clone the repository**
git clone https://github.com/Muhammad-Zubair796/ATS-Resume-Expert.git
cd ATS-Resume-Expert

**2. Create a Virtual Environment**
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Mac/Linux:
source .venv/bin/activate

**3. Install Dependencies**
pip install -r requirements.txt

**4. Set up your Environment Variables**
Create a file named `.env` in the root directory of the project and add your Google Gemini API key:
GOOGLE_API_KEY="your_google_api_key_here"
*(Note: The `.env` file is included in `.gitignore` to keep your API key secure. Never upload your API key to GitHub!)*

**5. Run the Application**
streamlit run app.py

---

## 💡 How to Use

1. Open the application in your web browser (usually `http://localhost:8501`).
2. Paste the target **Job Description** into the text area.
3. Upload the candidate's **Resume** in PDF format.
4. Click **"Tell Me About the Resume"** for a detailed HR evaluation.
5. Click **"Percentage Match"** to see the ATS score and missing keywords.

---

## 👨‍💻 Author

Developed by **Muhammad Zubair**
- GitHub: [@Muhammad-Zubair796](https://github.com/Muhammad-Zubair796)