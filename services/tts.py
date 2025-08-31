# services/tts.py
import requests
from typing import List, Dict, Any
from config import MURF_API_KEY
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

MURF_API_URL = "https://api.murf.ai/v1"

# Ensure uploads folder exists
UPLOADS_DIR = Path(__file__).resolve().parent.parent / "uploads"
UPLOADS_DIR.mkdir(exist_ok=True)


def speak(text: str, output_file: str = "stream_output.wav") -> bytes:
    """
    Convert text to speech using Murf API and save audio in uploads folder.
    NOTE: Murf API does not provide a streaming SDK publicly,
    so this uses the REST API and saves the resulting audio.
    """
    if not MURF_API_KEY:
        raise Exception("MURF_API_KEY not configured.")

    headers = {"Content-Type": "application/json", "api-key": MURF_API_KEY}
    payload = {
        "text": text,
        "voiceId": "en-US-ken",   # Default voice
        "format": "WAV",
        "style": "Conversational"
    }

    response = requests.post(f"{MURF_API_URL}/speech/generate", json=payload, headers=headers)
    response.raise_for_status()
    response_data = response.json()

    audio_url = response_data.get("audioFile")
    if not audio_url:
        raise Exception(f"Murf API did not return audioFile: {response_data}")

    # Download audio
    audio_response = requests.get(audio_url)
    audio_response.raise_for_status()
    audio_bytes = audio_response.content

    file_path = UPLOADS_DIR / output_file
    with open(file_path, "wb") as f:
        f.write(audio_bytes)

    return audio_bytes


def convert_text_to_speech(text: str, voice_id: str = "en-US-natalie") -> str:
    """Converts text to speech using Murf AI and returns audio file URL."""
    if not MURF_API_KEY:
        raise Exception("MURF_API_KEY not configured.")

    headers = {"Content-Type": "application/json", "api-key": MURF_API_KEY}
    payload = {
        "text": text,
        "voiceId": voice_id,
        "format": "MP3",
        "volume": "100%"
    }
    response = requests.post(f"{MURF_API_URL}/speech/generate", json=payload, headers=headers)
    response.raise_for_status()
    response_data = response.json()
    return response_data.get("audioFile")


def get_available_voices() -> List[Dict[str, Any]]:
    """Fetches the list of available voices from Murf AI."""
    if not MURF_API_KEY:
        raise Exception("MURF_API_KEY not configured.")

    headers = {"Accept": "application/json", "api-key": MURF_API_KEY}
    response = requests.get(f"{MURF_API_URL}/voices", headers=headers)
    response.raise_for_status()
    return response.json()
