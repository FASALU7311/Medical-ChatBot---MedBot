# 🩺 MedBot — Intelligent Medical Chatbot
**Overview**
<a href="https://github.com/404"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>

MedBot is a lightweight, AI-powered medical chatbot designed to provide basic healthcare advice and symptom analysis.
Built with Flask, HTML/CSS/JS, and optionally powered by advanced models like Bio_ClinicalBERT and Gemini AI, MedBot assists users by answering medical queries related to common symptoms and diseases.

⚡ Note: MedBot is NOT a replacement for professional medical advice.
<a href="https://github.com/404"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>


# Features
✅ Real-time symptom analysis

✅ Pre-defined responses for 40+ common diseases

✅ Smart symptom keyword extraction

✅ Gemini AI integration (Optional - for advanced diagnosis)

✅ Mobile-friendly and elegant UI

✅ Easy-to-deploy Flask backend

✅ Secure API key management using .env

<a href="https://github.com/404"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>

# Technologies Used
**Frontend:**

* HTML
* CSS
* JavaScript

**Backend:**

* Python 
* Flask
* HuggingFace Transformers (for Bio_ClinicalBERT)
* Google Gemini API (optional)

**Tools:**

* dotenv (for environment variables)
* PyTorch (for model loading)

<a href="https://github.com/404"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>

# Project Structure

```

MedBot/
│
├── __pycache__/                 # Python cache files (auto-generated)
│
├── js/
│   └── script.js                 # JavaScript for handling frontend requests
│
├── templates/
│   └── index.html                # Main frontend HTML file
│
├── venv/                         # Python virtual environment (auto-generated, don't push to GitHub)
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   └── ... (other venv files)
│
├── .gitignore                    # Git ignore file (to ignore venv, __pycache__, etc.)
├── .env                          # Environment variables (API keys like GEMINI_API_KEY)
├── app.py                        # Main Flask application
├── clinicalbert.py               # Symptom extraction using Bio_ClinicalBERT
├── gemini.py                     # Medical advice generation using Gemini AI
├── requirments.txt               # (Typo!) Should be: requirements.txt - list of dependencies

```
<a href="https://github.com/404"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>

<a href="https://github.com/404"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>

