# Voice-Agent

## Project Overview:
This is a voice agent that can speak in languages configured in the code; it currently uses an open‑source TTS model that speaks English fluently and provides basic multilingual support.

## Workflow
User voice detection < transcript via STT < LLM Transcript processing < TTS Voice Output
Note: If mic not available you can also type the query in CLI

## Project Specification
Modularity: All Device (Can work in windows, Mac OS and Linux)
Multi Language Support: English, Hindi, French, Spanish
TTS model used: Kokoro TTS 82M https://huggingface.co/spaces/hexgrad/Kokoro-TTS
STT Model: OpenAI Whisper-small https://github.com/openai/whisper
LLM Model: Perplexity Sonar via API https://perplexity.ai/sonar

## Project Status
Project completion: 25%
Project Modularity: Cross Device Support
Hardware Requirements: 500MB VRAM, 4 Core CPU, 4GB RAM
Python version: 3.12
Recommended Python environment: Ananconda or Minionda
Compactible Python environment: Poetry, Traditional system Venv

## Project Setup
1. Clone the repository
2. Install dependencies via requirements.txt (Conda) or poetry shell (Poetry)
3. keep the environment the PPLX_API_KEY in environment variables
4. Run the main.py to start the application
