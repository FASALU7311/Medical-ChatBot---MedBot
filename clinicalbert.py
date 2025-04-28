from transformers import AutoTokenizer, AutoModel
import torch

# Load Bio_ClinicalBERT
tokenizer = AutoTokenizer.from_pretrained("emilyalsentzer/Bio_ClinicalBERT")
model = AutoModel.from_pretrained("emilyalsentzer/Bio_ClinicalBERT")

# Sample list of known symptoms/diseases (expandable)
SYMPTOM_KEYWORDS = [
    "fever", "headache", "flu", "cough", "diabetes", "hypertension", "asthma", "allergy",
    "anemia", "pneumonia", "arthritis", "diarrhea", "migraine", "depression", "anxiety",
    "chickenpox", "measles", "dengue", "congestion", "malaria", "typhoid",
    "jaundice", "ulcer", "eczema", "psoriasis", "sinusitis",
    "bronchitis", "hepatitis", "kidney stone", "gallstones", "fracture", "sprain",
    "burn", "covid" ,"food poisoning","appendicitis" ,"obesity" ,"insomnia",
    "ear infection", "eye infection"
]

def extract_keywords(text):
    """Extract symptom keywords from text using keyword matching for now"""
    lower_text = text.lower()
    found = [kw for kw in SYMPTOM_KEYWORDS if kw in lower_text]
    return list(set(found))  # remove duplicates
