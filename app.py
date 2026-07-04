import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
import google.generativeai as genai

# --------------------
# Page Config
# --------------------
st.set_page_config(page_title="HR AI Assistant", layout="wide")

st.title("🤖 HR AI Assistant")

# --------------------
# Load Data
# --------------------
df = pd.read_csv("IBM-HR-Analytics.csv")

# --------------------
# Gemini API
# --------------------
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

# --------------------
# Sidebar
# --------------------

st.sidebar.title("Quick Questions")

question = st.sidebar.selectbox(
    "Choose",
    [
        "Custom Question",
        "Which department has highest attrition?",
        "What is the overall attrition rate?",
        "Which age group has highest attrition?",
        "Does overtime affect attrition?",
        "Which salary group loses most employees?",
        "Give recommendations to reduce attrition"
    ]
)
if question == "Custom Question":
    question = st.text_input("Ask your HR question")

st.write("---")
if st.button("Ask"):

    sample = df.head(100).to_string()

    prompt = f"""
You are an HR Data Analyst.

Here is part of an HR dataset:

{sample}

Use ONLY this data to answer.

Question:
{question}

Explain in simple business language.
"""

    response = model.generate_content(prompt)

    st.subheader("🤖 AI Answer")

    st.write(response.text)