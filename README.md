# Speech-to-Text Demo

This project provides a simple Flask-based web server that sends audio files to the ChatGPT API for transcription. It supports the `gpt-4o-mini-transcribe` and `gpt-4o-transcribe` models, and allows customization of the API `base_url` and `api_key` at runtime.

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running

```bash
python app.py
```

Visit `http://localhost:5001` in your browser. The interface now includes a microphone button so you can record audio directly in the page, or upload an existing file. Provide your API key, optionally override the base URL, choose a model, and submit the audio to receive a transcription.
