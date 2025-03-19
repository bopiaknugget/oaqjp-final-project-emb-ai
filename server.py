from flask import Flask, request, jsonify, json, make_response
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["POST"])
def detect():
    
    req_data = request.json
    text = req_data.get("text", "") 
    response = emotion_detector(text)   
    

    res_data = json.loads(response)

    if res_data['dominant_emotion'] is None :
        return make_response(" Invalid text! Please try again!",400)

    f"'anger': { res_data['anger']}, "
    f"'disgust': { res_data['disgust']}, "
    f"'fear': { res_data['fear']}, "
    f"'joy': { res_data['joy']} and "
    f"'sadness': { res_data['sadness']}. "
    f"The dominant emotion is { res_data['dominant_emotion']}."
    

    return output

if __name__ == "__main__":
    app.run()