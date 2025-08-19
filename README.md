# AI-Based-Interview
AI Voice Interview Application
This project is a voice-driven AI interview system built with a FastAPI backend and a JavaScript frontend that uses the browser's camera, microphone, and speech recognition capabilities. It enables a continuous conversation style interview with AI-generated questions and voice replies.

Features:
FastAPI backend that manages an interview process with predefined questions.

Sends questions one by one, records user answers, and presents an interview summary at the end.

Frontend with camera preview and microphone access.

Uses Web Speech API for voice recognition (speech-to-text) and text-to-speech.

Enables continuous voice conversation without repeatedly prompting for microphone permissions.

Simple, clean UI for ease of user interaction.

Technologies Used:
Python 3 with FastAPI

HTML, CSS, JavaScript (Web Speech API, MediaDevices API)

CORS middleware for cross-origin resource sharing

Setup & Usage
Backend
Install Python 3.9+ and pip.

Install required packages:

text
pip install fastapi uvicorn
Place the backend code (main.py) in your project directory.

Run the backend server:

text
uvicorn main:app --reload
The backend will start on http://localhost:8000.

Frontend
Place the frontend HTML (index.html) in your project directory.

Open index.html in the latest Chrome or Edge browser (required for full Web Speech API support).

Allow browser permissions for camera and microphone when prompted.

Use the Start/Stop Camera buttons to enable or disable video feed preview.

Click Start Listening once to grant microphone access and begin continuous voice interview.

Speak when prompted; the AI will respond with voice and text.

Click Stop Listening to end the session.

Project Structure
text
├── main.py          # FastAPI backend code
├── index.html       # Frontend HTML, CSS, and JS
├── README.md        # This file
Important Notes
The backend uses a fixed set of interview questions; you can customize or expand them in main.py.

The frontend manages mic permission requests once and uses continuous speech recognition for uninterrupted listening.

Supported browsers: Chrome and Edge (latest versions recommended)

Make sure both frontend and backend run on the same machine or adjust backend URL in the frontend fetch calls accordingly.

For production, configure CORS origins and secure endpoints.

Troubleshooting
Microphone prompts repeatedly: The browser asks permission once on starting recognition continuously. Clear site permissions if problems persist.

Speech recognition doesn’t start: Ensure the page is served over HTTPS or localhost and microphone is enabled in browser settings.

Backend fetch errors: Verify FastAPI server is running and accessible at the URL used in the frontend (http://localhost:8000/chat).

No AI reply or “Thinking...” stays forever: Check backend logs and network connectivity.

