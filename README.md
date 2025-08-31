<div align="center">
    <!-- Project logo placeholder -->
    <h1>BYTE - AI Voice Assistant</h1>
    <p>
        A real-time, multi-persona, and multi-skilled conversational AI voice assistant built with Python, FastAPI, and a powerful stack of modern AI services.
    </p>
    <p>
        <!-- Live demo badge -->
        <a href="https://zarex-ai.onrender.com/" target="_blank">
            <img src="/image.png" alt="Live Demo">
        </a>
    </p>
    <p>
        <!-- Technology badges -->
        <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
        <img src="https://img.shields.io/badge/FastAPI-green?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
        <img src="https://img.shields.io/badge/Docker-blue?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
        <img src="https://img.shields.io/badge/Deployed%20on-Render-lightgrey?style=for-the-badge&logo=render&logoColor=white" alt="Render">
    </p>
</div>

---

## 🧭 Table of Contents

- [Quickstart](#quickstart)
- [Environment & Config](#environment--config)
- [Architecture](#architecture)
- [Core Features](#core-features)
- [Project Structure](#project-structure)
- [Deployment](#deployment)
- [License](#license)

---

## Quickstart

You can run BYTE locally or deploy it to the cloud.

### Local Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Ekansh0718/murf-ai-challenge.git
   cd murf-ai-challenge/day-27
   ```

2. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**

   ```bash
   uvicorn app:app --reload
   ```

5. **Configure in Browser:**
   - Navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - Click the settings icon (⚙️) to enter your API keys and select a persona.

---

## Environment & Config

Create a `.env` file in your project root and add your API keys:

```
MURF_API_KEY="your_murf_api_key_here"
ASSEMBLYAI_API_KEY="your_assemblyai_api_key_here"
GEMINI_API_KEY="your_gemini_api_key_here"
SERPAPI_API_KEY="your_serpapi_key_here"
OPENWEATHER_API_KEY="your_openweather_api_key_here"
```

---

## Architecture

| Category          | Technology                                       |
| ----------------- | ------------------------------------------------ |
| **Backend**       | Python, FastAPI                                  |
| **Frontend**      | HTML, CSS, JavaScript                            |
| **AI & Services** | Gemini, Murf AI, SerpApi, WeatherAPI, AssemblyAI |
| **Deployment**    | Docker, Render                                   |

### ⚙️ Architecture Flow

```
┌───────────────┐       ┌────────────────────┐      ┌───────────────────────────┐
│ User Voice    │ ───>  │ STT (AssemblyAI)   │ ───> │ Backend (FastAPI)         │
└───────────────┘       └────────────────────┘      │ ↳ Skill & Persona Logic   │
                                                    └───────────┬───────────────┘
                                                                │
                                   ┌────────────────────────────┼───────────────────────────┐
                                   ▼                            ▼                           ▼
                                ┌───────────────────┐      ┌───────────────────┐      ┌───────────────────┐
                                │ LLM (Gemini)      │      │ Web Search (SerpApi)│   │ Weather (WeatherAPI)
                                └─────────┬─────────┘      └─────────┬─────────┘      └─────────┬─────────┘
                                          └──────────────────────────┼──────────────────────────┘
                                                                     |
                                                                     |
                                                                     ▼
                                        ┌───────────────────┐      ┌───────────────────┐
                                        │ Voice Response    │ <─── │ TTS (Murf AI)     │
                                        └───────────────────┘      └───────────────────┘
```

---

## Core Features

BYTE is not just a simple bot; it's a feature-rich voice assistant designed for a dynamic and interactive user experience.

- **🎙️ Real-time Voice Interaction:** Fluid, real-time conversation with minimal latency using WebSockets.
- **🧠 Intelligent & Context-Aware AI:** Session-based memory powered by Google Gemini.
- **🎭 Switchable AI Personas:** Instantly change the assistant's personality:
  - **Zarex:** Witty and sophisticated (default)
  - **Tutor:** Friendly and encouraging teacher
  - **Comedian:** Sarcastic and humorous companion
- **🔊 Natural & Realistic Voice:** High-quality, expressive voice responses via Murf AI.
- **🌐 Multi-Skilled Agent:** Performs various tasks:
  - **Live Web Search:** Real-time info via SerpApi
  - **Weather Updates:** Current weather via WeatherAPI
- **⚙️ Dynamic UI Configuration:** Enter API keys directly in the browser—no `.env` file needed!
- **☁️ Cloud Native:** Fully containerized with Docker and deployed on Render.

---

## Project Structure

```
/project-folder/
├── app.py
├── .env
├── requirements.txt
├── Dockerfile
├── /static/
│   └── script.js
├── /templates/
│   └── index.html
├── /services/
│   ├── llm.py
│   ├── stt.py
│   ├── tts.py
│   └── weather.py
└── /uploads/
```

---

## Deployment

### 🐳 Docker & Cloud

This application is ready for cloud deployment on platforms like Render.


1. **Deploy on Render:**
   - Push the code (including the Dockerfile) to a GitHub repository.
   - Create a new "Web Service" on Render and connect your repository.
   - Render will automatically detect the Dockerfile and deploy your application.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
