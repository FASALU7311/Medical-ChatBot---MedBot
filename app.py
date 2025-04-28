from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dummy function to simulate answering
def answer_query(question):
    question = question.lower()
    
    if "headache" in question:
        return "For headache, stay hydrated and rest. If it persists, consult a doctor."
    elif "fever" in question:
        return "Monitor your temperature and stay hydrated. Use paracetamol if needed."
    elif "cold" in question:
        return "Rest, drink warm fluids, and take vitamin C. Visit a doctor if symptoms worsen."
    elif "cough" in question:
        return "Stay hydrated, avoid cold drinks, and take cough syrup if necessary."
    elif "flu" in question:
        return "Rest, stay warm, and drink plenty of fluids. Consult a doctor if symptoms worsen."
    elif "diabetes" in question:
        return "Maintain a healthy diet, monitor blood sugar, and follow your medication routine."
    elif "hypertension" in question:
        return "Reduce salt intake, manage stress, exercise regularly, and take prescribed medications."
    elif "asthma" in question:
        return "Avoid triggers, carry an inhaler, and follow your doctor's treatment plan."
    elif "allergy" in question:
        return "Identify and avoid allergens. Antihistamines can help in mild cases."
    elif "anemia" in question:
        return "Increase iron-rich foods like spinach, red meat, and consult a doctor for supplements."
    elif "pneumonia" in question:
        return "Seek immediate medical attention. Antibiotics and rest are usually required."
    elif "arthritis" in question:
        return "Exercise gently, manage weight, and consider anti-inflammatory medications."
    elif "migraine" in question:
        return "Rest in a dark, quiet room. Over-the-counter pain relievers might help."
    elif "depression" in question:
        return "Talk to a mental health professional. Therapy and medications can help."
    elif "anxiety" in question:
        return "Practice breathing exercises, mindfulness, and seek professional counseling if needed."
    elif "covid" in question:
        return "Isolate yourself, monitor symptoms, stay hydrated, and seek medical help if severe."
    elif "chickenpox" in question:
        return "Rest, use calamine lotion for itching, and avoid scratching the blisters."
    elif "measles" in question:
        return "Rest, stay hydrated, and consult a doctor immediately."
    elif "dengue" in question:
        return "Stay hydrated, rest, and monitor for warning signs like bleeding or severe pain."
    elif "malaria" in question:
        return "Seek immediate medical treatment. Prevent mosquito bites in future."
    elif "typhoid" in question:
        return "Take prescribed antibiotics and stay hydrated."
    elif "jaundice" in question:
        return "Avoid fatty foods, stay hydrated, and follow medical advice."
    elif "ulcer" in question:
        return "Avoid spicy foods, alcohol, and take doctor-prescribed medications."
    elif "eczema" in question:
        return "Moisturize regularly and avoid known irritants. Consult a dermatologist."
    elif "psoriasis" in question:
        return "Use medicated creams and moisturizers. Light therapy can also help."
    elif "sinusitis" in question:
        return "Use nasal sprays, stay hydrated, and try warm compresses on your face."
    elif "bronchitis" in question:
        return "Rest, drink plenty of fluids, and avoid smoking."
    elif "hepatitis" in question:
        return "Avoid alcohol, eat healthy, and follow medical advice."
    elif "kidney stone" in question:
        return "Drink plenty of water and consult a doctor if severe pain occurs."
    elif "gallstones" in question:
        return "Surgery might be required. Consult a healthcare provider."
    elif "fracture" in question:
        return "Immobilize the area and seek immediate medical care."
    elif "sprain" in question:
        return "Rest, ice, compression, and elevation (RICE method)."
    elif "burn" in question:
        return "Cool the area with running water. Do not apply ice directly."
    elif "food poisoning" in question:
        return "Stay hydrated, rest, and seek medical help if symptoms are severe."
    elif "appendicitis" in question:
        return "Seek emergency medical attention; surgery may be necessary."
    elif "obesity" in question:
        return "Adopt a healthy diet and exercise regularly. Consult a dietitian if needed."
    elif "insomnia" in question:
        return "Maintain a sleep routine, avoid caffeine late in the day, and relax before sleeping."
    elif "ear infection" in question:
        return "Consult a doctor. Antibiotics may be necessary."
    elif "eye infection" in question:
        return "Use prescribed eye drops and avoid touching the eyes."

    else:
        return "I'm a simple MedBot. Please ask about common symptoms or known diseases."


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form['question']
    response = answer_query(question)
    return jsonify(answer=response)

if __name__ == '__main__':
    app.run(debug=True)
