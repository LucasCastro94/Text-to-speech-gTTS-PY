from gtts import gTTS
from io import BytesIO
from flask import Flask, request, send_file


app = Flask(__name__)

@app.route('/synthesize', methods=['POST'])
def synthesize():
    text = request.json.get('text')

    # Gerar o áudio usando o mecanismo gTTS
    tts = gTTS(text, lang='pt-br')
    audio_stream = BytesIO()
    tts.save(audio_stream)
    audio_stream.seek(0)
    
    print(audio_stream)

    # Retornar o áudio como resposta
    return send_file(audio_stream, mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
