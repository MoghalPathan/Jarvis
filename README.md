# Jarvis - Python Voice Assistant

Jarvis is a voice assistant built with Python. Say **"Jarvis"** once to wake it up, and it keeps listening for commands until you tell it to sleep or exit.

## Features

- Wake word activation ("Jarvis"), then continuous listening
- Open websites by voice (Google, YouTube, GitHub, Gmail)
- Play songs from your own music library
- Get the current weather (OpenWeatherMap)
- Answer general questions with AI (Google Gemini)
- Text-to-speech replies

## Tech Stack

- Python 3.10
- SpeechRecognition + PyAudio (speech to text)
- pyttsx3 (text to speech)
- Google Gemini API (AI answers)
- OpenWeatherMap API (weather)

## Project Structure

```
Mega Project1/
├── main.py             # main assistant code
├── musicLibrary.py     # song name -> link dictionary
├── requirements.txt    # Python dependencies
├── .env                # API keys (NOT uploaded to GitHub)
└── .gitignore
```

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/MoghalPathan/Jarvis.git
cd Jarvis
```

**2. Create and activate a virtual environment**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Add your API keys**

Create a file named `.env` in the project folder:
```
GEMINI_API_KEY=your_gemini_key_here
WEATHER_API_KEY=your_openweathermap_key_here
```

- Gemini key: https://aistudio.google.com/apikey
- Weather key: https://openweathermap.org (new keys can take 1-2 hours to activate)

**5. Create `musicLibrary.py`**
```python
music = {
    "song1": "https://www.youtube.com/watch?v=...",
    "song2": "https://www.youtube.com/watch?v=...",
}
```

**6. Run**
```bash
python main.py
```

## How to Use

1. Say **"Jarvis"** and wait for "Yes sir".
2. Give commands. No need to say "Jarvis" again.

| Command | What it does |
|---|---|
| "open Google / YouTube / GitHub / email" | Opens the website |
| "play song1" | Opens the song link from `musicLibrary.py` |
| "weather" or "temperature" | Speaks the current weather |
| Any other question | Answered by Gemini AI |
| "stop listening" | Jarvis goes back to sleep (wake word needed again) |
| "exit" | Closes the program |

## Notes

- An internet connection is required for speech recognition, weather and AI answers.
- Never upload your `.env` file. It is listed in `.gitignore`.
- Speak clearly and close to the microphone for best results.

## Author

Made by Korabu Naved Arif
