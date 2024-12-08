from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector  # Import the emotion detector function

app = Flask(__name__)

@app.route('/')
def index():
    # This will render the index.html template located in the templates folder
    return render_template('templates/index.html')




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)