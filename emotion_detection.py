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
        return response.json().get('text', 'No text found in the response')
        print(response)
    else:
        return f"Error: {response.status_code}"



# Example usage of the function
if __name__ == "__main__":
    text_to_analyze = "I love this new technology."
    result = emotion_detector(text_to_analyze)
    print(result)