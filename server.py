from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector  # Import the emotion detector function

app = Flask(__name__)


def error_handling_function(text):
    # Check if the input is empty or only whitespace
    if not text.strip():  
        return jsonify({"message": "Invalid text! Please try again!"}), 400  # Return 400 Bad Request response
    

@app.route('/')
def index():
    # This will render the index.html template located in the templates folder
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    text_to_analyze = request.form['textToAnalyze']  # The name of the input field in the HTML form
    print(text_to_analyze)

    error_response = error_handling_function(text_to_analyze)
    if error_response:  # If the error response is triggered, stop processing further
        return error_response


    emotion_scores = emotion_detector(text_to_analyze)
    dominant_emotion = emotion_scores['dominant_emotion']
    emotion_message = (
            f"For the given statement, the system response is "
            f"'anger': {emotion_scores['anger']}, "
            f"'disgust': {emotion_scores['disgust']}, "
            f"'fear': {emotion_scores['fear']}, "
            f"'joy': {emotion_scores['joy']} and "
            f"'sadness': {emotion_scores['sadness']}. "
            f"The dominant emotion is {dominant_emotion}."
    )
    # Return the result as JSON
    print(emotion_message)
    return jsonify({"message": emotion_message})



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)