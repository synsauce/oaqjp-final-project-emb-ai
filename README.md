# Emotion Detection Web Application

Final project for **IBM’s "Developing AI Applications with Python and Flask"** course, part of the 
[IBM AI Developer Professional Certificate](https://www.coursera.org/professional-certificates/ibm-ai-developer) through Coursera.

---

## Project Overview
This project implements a simple **NLP Emotion Detection web application** using:
- **Python** (core logic)
- **Flask** (backend web framework)
- **HTML/CSS/JavaScript** (frontend)
- **IBM Watson NLP EmotionPredict API** (to analyze text for emotions)

The app allows users to enter text in a web form and receive emotion predictions (anger, disgust, fear, joy, sadness) along with the **dominant emotion**.

---

## Features
- Web UI built with Flask and vanilla JS.
- Integration with IBM Watson NLP EmotionPredict service.
- Handles invalid/blank input with custom error messages.
- Returns results in a clean, human-readable format.

---

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/synsauce/oaqjp-final-project-emb-ai.git
   cd oaqjp-final-project-emb-ai

2. **Clone the repository**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

4. **Run the Flask app**:
   ```bash
   python server.py

5. **Open the app in your browser at**:
   ```url
   http://localhost:5000

---

## Project Structure

├── EmotionDetection/
│   └── emotion_detection.py   # Core emotion detection function
├── static/
│   └── mywebscript.js         # Frontend JS
├── templates/
│   └── index.html             # Web UI
├── server.py                  # Flask backend
├── requirements.txt           # Dependencies
└── README.md                  # Read Me

---

## Acknowledgments

- IBM Skills Network for providing the Watson NLP EmotionPredict service.

- Coursera & IBM for the AI Developer Specialization.

- Project developed as part of the Final Project for "Developing AI Applications with Python and Flask".
