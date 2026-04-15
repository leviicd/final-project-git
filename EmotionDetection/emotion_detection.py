import requests
import json

def emotion_detector(text_to_analyse):
    # URL layanan API Watson NLP untuk deteksi emosi
    url = 'https://sn-watson-emotion.p.cloud.ibm.com/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Header yang diperlukan oleh API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Objek data yang akan dikirim dalam format JSON
    myobj = { "raw_document": { "content": text_to_analyse } }
    
    # Mengirim permintaan POST ke API
    response = requests.post(url, json=myobj, headers=header)
    
    # Mengubah format respon teks menjadi dictionary Python menggunakan json.loads
    formatted_response = json.loads(response.text)

    # Mengekstrak emosi dari respon (Asumsi status code 200/Sukses)
    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        
        # Menentukan emosi dominan (nilai tertinggi)
        dominant_emotion = max(emotions, key=emotions.get)
        
        # Mengembalikan hasil sesuai format yang diminta di Task 3
        return {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }
    
    # Jika input kosong atau status code 400 (Terkait Task 7)
    elif response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
