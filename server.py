from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    text = (request.args.get("textToAnalyze") or "").strip()
    result = emotion_detector(text)

    if result.get("dominant_emotion") is None:
        # Choose ONE of these depending on your frontend:
        # return "Invalid text! Please try again!", 400   # semantic, requires JS to read 400
        return "Invalid text! Please try again!", 200 # simplest if JS only renders 200s

    response_text = (
        "For the given statement, the system response is "
        f"'anger': {result['anger']:.9f}, "
        f"'disgust': {result['disgust']:.9f}, "
        f"'fear': {result['fear']:.9f}, "
        f"'joy': {result['joy']:.9f} and "
        f"'sadness': {result['sadness']:.9f}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response_text, 200

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)