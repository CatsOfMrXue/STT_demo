from flask import Flask, request, render_template_string, jsonify
from openai import OpenAI
import io

app = Flask(__name__)

HTML_FORM = """
<!doctype html>
<title>Speech to Text Demo</title>
<h1>Upload audio for transcription</h1>
<form method="post" enctype="multipart/form-data" action="/transcribe">
  Base URL: <input type="text" name="base_url" value="https://api.openai.com/v1"><br>
  API Key: <input type="text" name="api_key"><br>
  Model: <select name="model">
    <option value="gpt-4o-mini-transcribe">gpt-4o-mini-transcribe</option>
    <option value="gpt-4o-transcribe">gpt-4o-transcribe</option>
  </select><br>
  Audio File: <input type="file" name="audio"><br>
  <input type="submit" value="Transcribe">
</form>
"""

@app.route('/', methods=['GET'])
def index():
    return render_template_string(HTML_FORM)

@app.route('/transcribe', methods=['POST'])
def transcribe():
    api_key = request.form.get('api_key')
    base_url = request.form.get('base_url') or "https://api.openai.com/v1"
    model = request.form.get('model', 'gpt-4o-mini-transcribe')
    audio = request.files.get('audio')

    if not api_key or audio is None:
        return "Missing API key or audio file", 400

    client = OpenAI(api_key=api_key, base_url=base_url)

    audio_bytes = audio.read()
    buf = io.BytesIO(audio_bytes)
    buf.name = audio.filename or 'audio.wav'

    try:
        result = client.audio.transcriptions.create(
            model=model,
            file=buf
        )
        text = result.text
    except Exception as e:
        return f"Error: {e}", 500

    return jsonify({"text": text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
