import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


import google.generativeai as genai
import re


def clean_response(text):
    # Remove all markdown-like formatting (bold/italic)
    text = re.sub(r'(\*{1,2}|_{1,2})', '', text)
    text = re.sub(r'\n{2,}', '\n\n', text).strip()
    return text

def structure_response(text):
    cleaned = clean_response(text)

    sections = {
        "Possible Conditions": [],
        "Medications": [],
        "When to See a Doctor": [],
        "Note": []
    }

    current_section = None
    for line in cleaned.split('\n'):
        lower = line.lower()

        if "possible condition" in lower:
            current_section = "Possible Conditions"
        elif "medication" in lower or "over-the-counter" in lower:
            current_section = "Medications"
        elif "see a doctor" in lower or "important consideration" in lower:
            current_section = "When to See a Doctor"
        elif "note" in lower or "this information" in lower:
            current_section = "Note"
        elif current_section:
            sections[current_section].append(line.strip())

    # Build final structured output
    result = ""
    for section, content in sections.items():
        if content:
            result += f"\n\n🟢 {section}:\n" + "\n".join(content)

    return result.strip()

def get_medical_advice(symptoms_list):
    prompt = (
        "I have the following symptoms: " + ", ".join(symptoms_list) +
        ". Please provide step-by-step advice including: Possible Conditions, Medications, "
        "donot forget to add  Possible Conditions and Medications "
        "must provide When to See a Doctor. Avoid using markdown (no asterisks, no formatting)."
        
    )
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content(prompt)
    return structure_response(response.text)
