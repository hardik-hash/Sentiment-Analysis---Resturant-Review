{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2cc439fb",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk\n",
    "from tkinter import ttk\n",
    "import speech_recognition as sr\n",
    "from nltk.sentiment import SentimentIntensityAnalyzer\n",
    "\n",
    "# Download NLTK resources if not already downloaded\n",
    "import nltk\n",
    "nltk.download('vader_lexicon')\n",
    "\n",
    "# Initialize the Sentiment Intensity Analyzer\n",
    "sia = SentimentIntensityAnalyzer()\n",
    "\n",
    "def analyze_voice_sentiment(audio):\n",
    "    \"\"\"Analyze the sentiment of speech input and return a sentiment label.\"\"\"\n",
    "    text = recognizer.recognize_google(audio)\n",
    "    scores = sia.polarity_scores(text)\n",
    "    if scores['compound'] >= 0.05:\n",
    "        return 'Positive'\n",
    "    elif scores['compound'] <= -0.05:\n",
    "        return 'Negative'\n",
    "    else:\n",
    "        return 'Neutral'\n",
    "\n",
    "def start_listening():\n",
    "    \"\"\"Start listening for speech input.\"\"\"\n",
    "    global listening\n",
    "    listening = True\n",
    "    status_label.config(text=\"Listening...\")\n",
    "\n",
    "def stop_listening():\n",
    "    \"\"\"Stop listening for speech input.\"\"\"\n",
    "    global listening\n",
    "    listening = False\n",
    "    status_label.config(text=\"Not Listening\")\n",
    "\n",
    "def process_audio():\n",
    "    \"\"\"Process the recorded audio for sentiment analysis.\"\"\"\n",
    "    while listening:\n",
    "        with sr.Microphone() as source:\n",
    "            audio = recognizer.listen(source)\n",
    "        try:\n",
    "            label = analyze_voice_sentiment(audio)\n",
    "            sentiment_label.config(text=f\"Sentiment: {label}\")\n",
    "        except sr.UnknownValueError:\n",
    "            sentiment_label.config(text=\"Could not understand audio\")\n",
    "        except sr.RequestError as e:\n",
    "            sentiment_label.config(text=f\"Error: {e}\")\n",
    "\n",
    "# Initialize Tkinter window\n",
    "root = tk.Tk()\n",
    "root.title(\"Speech Sentiment Analysis\")\n",
    "root.geometry(\"400x200\")\n",
    "\n",
    "# Create GUI elements\n",
    "status_label = ttk.Label(root, text=\"Not Listening\", font=(\"Arial\", 12))\n",
    "status_label.pack(pady=10)\n",
    "\n",
    "start_button = ttk.Button(root, text=\"Start Listening\", command=start_listening)\n",
    "start_button.pack()\n",
    "\n",
    "stop_button = ttk.Button(root, text=\"Stop Listening\", command=stop_listening)\n",
    "stop_button.pack()\n",
    "\n",
    "sentiment_label = ttk.Label(root, text=\"Sentiment: \", font=(\"Arial\", 12))\n",
    "sentiment_label.pack(pady=10)\n",
    "\n",
    "# Initialize SpeechRecognizer\n",
    "recognizer = sr.Recognizer()\n",
    "\n",
    "# Start processing audio asynchronously\n",
    "listening = False\n",
    "process_audio()\n",
    "\n",
    "# Start the Tkinter event loop\n",
    "root.mainloop()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "404f5c85",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk\n",
    "from tkinter import ttk\n",
    "import speech_recognition as sr\n",
    "from nltk.sentiment import SentimentIntensityAnalyzer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9c4e74ca",
   "metadata": {},
   "outputs": [],
   "source": [
    "sia = SentimentIntensityAnalyzer()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "bb80c927",
   "metadata": {},
   "outputs": [],
   "source": [
    "def analyze_voice_sentiment(audio):\n",
    "    \"\"\"Analyze the sentiment of speech input and return a sentiment label.\"\"\"\n",
    "    text = recognizer.recognize_google(audio)\n",
    "    scores = sia.polarity_scores(text)\n",
    "    if scores['compound'] >= 0.05:\n",
    "        return 'Positive'\n",
    "    elif scores['compound'] <= -0.05:\n",
    "        return 'Negative'\n",
    "    else:\n",
    "        return 'Neutral'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "7df28dd4",
   "metadata": {},
   "outputs": [],
   "source": [
    "def start_listening():\n",
    "    \"\"\"Start listening for speech input.\"\"\"\n",
    "    global listening\n",
    "    listening = True\n",
    "    status_label.config(text=\"Listening...\")\n",
    "\n",
    "def stop_listening():\n",
    "    \"\"\"Stop listening for speech input.\"\"\"\n",
    "    global listening\n",
    "    listening = False\n",
    "    status_label.config(text=\"Not Listening\")\n",
    "\n",
    "def process_audio():\n",
    "    \"\"\"Process the recorded audio for sentiment analysis.\"\"\"\n",
    "    while listening:\n",
    "        with sr.Microphone() as source:\n",
    "            audio = recognizer.listen(source)\n",
    "        try:\n",
    "            label = analyze_voice_sentiment(audio)\n",
    "            sentiment_label.config(text=f\"Sentiment: {label}\")\n",
    "        except sr.UnknownValueError:\n",
    "            sentiment_label.config(text=\"Could not understand audio\")\n",
    "        except sr.RequestError as e:\n",
    "            sentiment_label.config(text=f\"Error: {e}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "29429b4f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "''"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "root = tk.Tk()\n",
    "root.title(\"Speech Sentiment Analysis\")\n",
    "root.geometry(\"400x200\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "91b264ab",
   "metadata": {},
   "outputs": [],
   "source": [
    "status_label = ttk.Label(root, text=\"Not Listening\", font=(\"Arial\", 12))\n",
    "status_label.pack(pady=10)\n",
    "\n",
    "start_button = ttk.Button(root, text=\"Start Listening\", command=start_listening)\n",
    "start_button.pack()\n",
    "\n",
    "stop_button = ttk.Button(root, text=\"Stop Listening\", command=stop_listening)\n",
    "stop_button.pack()\n",
    "\n",
    "sentiment_label = ttk.Label(root, text=\"Sentiment: \", font=(\"Arial\", 12))\n",
    "sentiment_label.pack(pady=10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "6a99ffb1",
   "metadata": {},
   "outputs": [],
   "source": [
    "recognizer = sr.Recognizer()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "913bef34",
   "metadata": {},
   "outputs": [],
   "source": [
    "listening = False\n",
    "process_audio()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "2a482974",
   "metadata": {},
   "outputs": [],
   "source": [
    "root.mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "eb30be8c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk\n",
    "from tkinter import ttk\n",
    "import speech_recognition as sr\n",
    "from nltk.sentiment import SentimentIntensityAnalyzer\n",
    "\n",
    "# Download NLTK resources if not already downloaded\n",
    "import nltk\n",
    "\n",
    "# Initialize the Sentiment Intensity Analyzer\n",
    "sia = SentimentIntensityAnalyzer()\n",
    "\n",
    "def analyze_voice_sentiment(audio):\n",
    "    \"\"\"Analyze the sentiment of speech input and return a sentiment label.\"\"\"\n",
    "    text = recognizer.recognize_google(audio)\n",
    "    scores = sia.polarity_scores(text)\n",
    "    if scores['compound'] >= 0.05:\n",
    "        return 'Positive'\n",
    "    elif scores['compound'] <= -0.05:\n",
    "        return 'Negative'\n",
    "    else:\n",
    "        return 'Neutral'\n",
    "\n",
    "def start_listening():\n",
    "    \"\"\"Start listening for speech input.\"\"\"\n",
    "    global listening\n",
    "    listening = True\n",
    "    status_label.config(text=\"Listening...\")\n",
    "\n",
    "def stop_listening():\n",
    "    \"\"\"Stop listening for speech input.\"\"\"\n",
    "    global listening\n",
    "    listening = False\n",
    "    status_label.config(text=\"Not Listening\")\n",
    "\n",
    "def process_audio():\n",
    "    \"\"\"Process the recorded audio for sentiment analysis.\"\"\"\n",
    "    while listening:\n",
    "        with sr.Microphone() as source:\n",
    "            audio = recognizer.listen(source)\n",
    "        try:\n",
    "            label = analyze_voice_sentiment(audio)\n",
    "            sentiment_label.config(text=f\"Sentiment: {label}\")\n",
    "        except sr.UnknownValueError:\n",
    "            sentiment_label.config(text=\"Could not understand audio\")\n",
    "        except sr.RequestError as e:\n",
    "            sentiment_label.config(text=f\"Error: {e}\")\n",
    "\n",
    "# Initialize Tkinter window\n",
    "root = tk.Tk()\n",
    "root.title(\"Speech Sentiment Analysis\")\n",
    "root.geometry(\"400x200\")\n",
    "\n",
    "# Create GUI elements\n",
    "status_label = ttk.Label(root, text=\"Not Listening\", font=(\"Arial\", 12))\n",
    "status_label.pack(pady=10)\n",
    "\n",
    "start_button = ttk.Button(root, text=\"Start Listening\", command=start_listening)\n",
    "start_button.pack()\n",
    "\n",
    "stop_button = ttk.Button(root, text=\"Stop Listening\", command=stop_listening)\n",
    "stop_button.pack()\n",
    "\n",
    "sentiment_label = ttk.Label(root, text=\"Sentiment: \", font=(\"Arial\", 12))\n",
    "sentiment_label.pack(pady=10)\n",
    "\n",
    "# Initialize SpeechRecognizer\n",
    "recognizer = sr.Recognizer()\n",
    "\n",
    "# Start processing audio asynchronously\n",
    "listening = False\n",
    "process_audio()\n",
    "\n",
    "# Start the Tkinter event loop\n",
    "root.mainloop()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "49d534c0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "13fa35a6",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b4cea381",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8d6614de",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "338e21ad",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c22e6683",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1597b380",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0f108178",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "18c7b206",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "05a4629a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "437d0ca7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "04c1a52b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
