from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector  # Import the emotion detector function

# Initialize Flask app
app = Flask(__name__)

def error_handling_function(text):
    """
    This function checks if the input text is empty or only contains whitespace.
    If it is, it returns a 400 error with a message; otherwise, it returns None.
    """
    if not text.strip():  # Check if the input is empty or contains only whitespace
        return jsonify({"message": "Invalid text! Please try again!"}), 400  # Return 400 Bad Request response
    return None  # Return None if input is valid

@app.route('/')
def index():
    """
    Renders the index.html page for the user.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """
    This route handles the POST request for emotion detection.
    It retrieves the text to analyze, handles any errors, and returns the emotion analysis.
    """
    text_to_analyze = request.form['textToAnalyze']  # Get the input from the HTML form
    print(text_to_analyze)

    # First, check if the input is valid
    error_response = error_handling_function(text_to_analyze)
    if error_response:  # If the error response is triggered, stop further processing
        return error_response

    # Proceed with emotion detection if the input is valid
    emotion_scores = emotion_detector(text_to_analyze)
    dominant_emotion = emotion_scores['dominant_emotion']
    
    # Prepare the response message
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

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)