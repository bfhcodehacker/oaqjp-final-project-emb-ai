"""
    Basic Flask server for emotion detection project
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detection')

@app.route("/")
def render_index_page():
    """
        renders index page
        returns index.html
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detection():
    """
      returns emotion detector response
      return json object with emotion scores
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
