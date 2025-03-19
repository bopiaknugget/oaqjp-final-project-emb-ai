from flask import Flask, json
import requests
def error_handling_function(text) : 
    if text == "" or isinstance(text, type(None)) :
        return True
    return False

def emotion_detector(text_to_analyze):

    if(error_handling_function(text_to_analyze)) :

        result = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        return json.dumps(result, indent=4)

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    data = {
        "raw_document": {"text": text_to_analyze}
    }

    


    response = requests.post(url, headers=headers, json=data).json()
    emotions = response["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotions, key=emotions.get)
    
    result = {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion
    }

    return json.dumps(result, indent=4)

