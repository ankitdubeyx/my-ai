AI Assistant A lightweight, local web-based AI assistant interface built with Flask and designed to interact with local LLMs via Ollama.

Overview This application provides a simple, clean, and responsive chat interface in your browser. It sends user messages to a locally running Ollama instance, which processes the prompt and returns a response.

Prerequisites Before running this application, you must have the following installed:

Python 3.x
Ollama: Ensure Ollama is installed and running on your machine.
Model: You must have a model downloaded in Ollama (the code defaults to phi3).
You can download it by running: ollama pull phi3

Installation

Clone the repository:

git clone https://github.com/ankitdubeyx/my-ai.git cd my-ai

Install dependencies: It is recommended to use a virtual environment:

python -m venv venv source venv/bin/activate # On Windows: venv\Scripts\activate pip install flask requests

Running the App

Ensure Ollama is running in the background.
Start the Flask server:
python my-ai.py

Open your web browser and navigate to: (http://127.0.0.1:5000)
Configuration You can change the model used by updating the MODEL variable in my-ai.py. Ensure the model is already pulled into your Ollama instance.
