import requests
import json


def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    # Send the POST request to the Watson NLP API
    response = requests.post(url, headers=headers, json=data)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Return the text from the response JSON
        print("done")
        emotions = response.json()
        emotions = emotions['emotionPredictions'][0]['emotion']

        print(emotions)
        
                # Initialize emotion scores
        anger_score = emotions.get('anger', 0)
        disgust_score = emotions.get('disgust', 0)
        fear_score = emotions.get('fear', 0)
        joy_score = emotions.get('joy', 0)
        sadness_score = emotions.get('sadness', 0)
        
        # Create a dictionary to store the emotions and their scores
        emotion_scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }

        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

            # Add the dominant emotion to the result
        emotion_scores['dominant_emotion'] = dominant_emotion
        
        return emotion_scores


    else:
        return f"Error: {response.status_code}"



# Example usage of the function
if __name__ == "__main__":
    text_to_analyze = "I am glad this happened"
    result = emotion_detector(text_to_analyze)
    print(result)