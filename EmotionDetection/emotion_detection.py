"""
emotion_detection.py

Analyze emotions in text using the IBM Watson NLP Emotion Predict service.
Sends input text to the Watson endpoint and returns a dictionary containing
the five emotion scores and the dominant emotion.

Function:
    emotion_detector(text_to_analyze: str) -> dict
"""

import requests

WATSON_URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
HEADERS = {
    "Content-Type": "application/json",
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
}

ALL_NONE = {
    "anger": None,
    "disgust": None,
    "fear": None,
    "joy": None,
    "sadness": None,
    "dominant_emotion": None,
}

def emotion_detector(text_to_analyze: str) -> dict:
    """
    Analyze the emotional content of a text string using IBM Watson's
    NLP EmotionPredict service.

    Args:
        text_to_analyze (str): The input text to analyze. If blank or invalid,
            the function will return a dictionary with all values set to None.

    Returns:
        dict: A dictionary with the following keys:
            - 'anger' (float or None)
            - 'disgust' (float or None)
            - 'fear' (float or None)
            - 'joy' (float or None)
            - 'sadness' (float or None)
            - 'dominant_emotion' (str or None)

        When the input is valid, the float scores range from 0.0 to 1.0
        and 'dominant_emotion' is the label with the highest score.
        If the input is blank or the API returns an error, all values are None.
    """
    if not (text_to_analyze or "").strip():
        return ALL_NONE

    resp = requests.post(WATSON_URL, headers=HEADERS,
                        json={"raw_document": {"text": text_to_analyze}},
                        timeout=10)

    if resp.status_code == 400:
        return ALL_NONE

    if resp.status_code != 200:
        return ALL_NONE  # or log

    data = resp.json()
    emotions = data["emotionPredictions"][0]["emotion"]
    anger   = float(emotions.get("anger", 0.0))
    disgust = float(emotions.get("disgust", 0.0))
    fear    = float(emotions.get("fear", 0.0))
    joy     = float(emotions.get("joy", 0.0))
    sadness = float(emotions.get("sadness", 0.0))

    scores = {
    "anger": anger,
    "disgust": disgust,
    "fear": fear,
    "joy": joy,
    "sadness": sadness,
}

    dominant = max(scores, key=scores.get)

    return {"anger": anger, "disgust": disgust, "fear": fear, "joy": joy,
            "sadness": sadness, "dominant_emotion": dominant}
