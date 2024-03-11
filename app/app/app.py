from flask import (
    Blueprint, 
    render_template,
    request,
    Response
    )
import requests

bp = Blueprint('app', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


def get_google_tts(text, language='ja-JP', speed=1.0):
    # 在 Google Cloud Console 中创建项目并启用 Text-to-Speech API
    api_key = 'YOUR_GOOGLE_CLOUD_API_KEY'

    url = 'https://texttospeech.googleapis.com/v1/text:synthesize?key=' + api_key
    headers = {'Content-Type': 'application/json'}
    data = {
        "input": {"text": text},
        "voice": {"languageCode": language, "ssmlGender": "NEUTRAL"},
        "audioConfig": {"audioEncoding": "MP3", "speakingRate": speed}
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.content
    else:
        return None

@bp.route('/speak', methods=['GET', 'POST'])
def speak():
    text = request.form.get('text')
    speed = float(request.form.get('speed', 1.0))

    audio_data = get_google_tts(text, language='ja-JP', speed=speed)
    if audio_data:
        # 返回音频文件
        return Response(audio_data, mimetype='audio/mp3')
    else:
        return "Failed to get TTS audio", 500