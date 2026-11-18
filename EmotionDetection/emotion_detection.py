import requests
import json

error_scores = {
    'anger': None,
    'disgust': None,
    'fear': None,
    'joy': None,
    'sadness': None,
    'dominant_emotion': None
}

def emotion_detector(text_to_analyse): 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  
    myobj = { "raw_document": { "text": text_to_analyse } }  
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  
    response = requests.post(url, json = myobj, headers=header)
    if response.status_code == 200:
        json_response = json.loads(response.text)
        js = json_response['emotionPredictions'][0]['emotion']
        max_emotion = ''
        max_score = 0
        for key in js:
            if js[key] > max_score:
                max_score = js[key]
                max_emotion = key
        scores = {
            'anger': js['anger'],
            'disgust': js['disgust'],
            'fear': js['fear'],
            'joy': js['joy'],
            'sadness': js['sadness'],
            'dominant_emotion': max_emotion
        }
    elif response.status_code == 400:
        scores = error_scores
    else:
        scores = error_scores
    return scores