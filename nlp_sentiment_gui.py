{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a09df05f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk\n",
    "from tkinter import ttk\n",
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "from sklearn.svm import SVC\n",
    "import pandas as pd\n",
    "\n",
    "# Load the sentiment analysis dataset from a CSV file\n",
    "data = pd.read_csv('sentiment_data.csv')  # Replace 'your_dataset.csv' with your actual CSV file\n",
    "\n",
    "# Preprocess text data and extract features using TF-IDF vectorization\n",
    "vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')\n",
    "X = vectorizer.fit_transform(data['text'])\n",
    "y = data['sentiment']\n",
    "\n",
    "# Train a Support Vector Machine (SVM) classifier\n",
    "svm_classifier = SVC(kernel='linear')\n",
    "svm_classifier.fit(X, y)\n",
    "\n",
    "def predict_sentiment():\n",
    "    input_text = input_entry.get()\n",
    "    input_vectorized = vectorizer.transform([input_text])\n",
    "    predicted_sentiment = svm_classifier.predict(input_vectorized)\n",
    "    sentiment_mapping = {0: 'negative', 1: 'positive'}\n",
    "    predicted_sentiment_human_readable = sentiment_mapping[predicted_sentiment[0]]\n",
    "    sentiment_label.config(text=f\"Predicted Sentiment: {predicted_sentiment_human_readable}\")\n",
    "\n",
    "# Create a Tkinter window\n",
    "root = tk.Tk()\n",
    "root.title(\"Sentiment Analysis\")\n",
    "\n",
    "# Create GUI elements\n",
    "input_label = ttk.Label(root, text=\"Enter a sentence:\")\n",
    "input_label.pack(pady=10)\n",
    "\n",
    "input_entry = ttk.Entry(root, width=50)\n",
    "input_entry.pack()\n",
    "\n",
    "predict_button = ttk.Button(root, text=\"Predict\", command=predict_sentiment)\n",
    "predict_button.pack(pady=10)\n",
    "\n",
    "sentiment_label = ttk.Label(root, text=\"\")\n",
    "sentiment_label.pack()\n",
    "\n",
    "# Start the Tkinter event loop\n",
    "root.mainloop()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "54d1c5f6",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk\n",
    "from tkinter import ttk\n",
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "from sklearn.svm import SVC\n",
    "import pandas as pd\n",
    "\n",
    "# Load the sentiment analysis dataset from a CSV file\n",
    "data = pd.read_csv('sentiment_data.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d97e644c",
   "metadata": {},
   "outputs": [],
   "source": [
    "vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')\n",
    "X = vectorizer.fit_transform(data['text'])\n",
    "y = data['sentiment']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4549ca66",
   "metadata": {},
   "outputs": [],
   "source": [
    "svm_classifier = SVC(kernel='linear')\n",
    "svm_classifier.fit(X, y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "df7acb21",
   "metadata": {},
   "outputs": [],
   "source": [
    "def predict_sentiment():\n",
    "    input_text = input_entry.get()\n",
    "    if not input_text:\n",
    "        sentiment_label.config(text=\"Please enter a sentence.\")\n",
    "        return\n",
    "\n",
    "    input_vectorized = vectorizer.transform([input_text])\n",
    "    predicted_sentiment = svm_classifier.predict(input_vectorized)\n",
    "    sentiment_mapping = {'Negative': 'Negative', 'Positive': 'Positive', 'Neutral': 'Neutral'}\n",
    "\n",
    "    if predicted_sentiment[0] in sentiment_mapping:\n",
    "        predicted_sentiment_human_readable = sentiment_mapping[predicted_sentiment[0]]\n",
    "        sentiment_label.config(text=f\"Predicted Sentiment: {predicted_sentiment_human_readable}\")\n",
    "    else:\n",
    "        sentiment_label.config(text=\"Error: Unexpected sentiment prediction.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e5d2da8b",
   "metadata": {},
   "outputs": [],
   "source": [
    "root = tk.Tk()\n",
    "root.title(\"Sentiment Analysis\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2ea7db6d",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'ttk' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m input_label \u001b[38;5;241m=\u001b[39m \u001b[43mttk\u001b[49m\u001b[38;5;241m.\u001b[39mLabel(root, text\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mEnter a sentence:\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m      2\u001b[0m input_label\u001b[38;5;241m.\u001b[39mpack(pady\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m10\u001b[39m)\n\u001b[0;32m      4\u001b[0m input_entry \u001b[38;5;241m=\u001b[39m ttk\u001b[38;5;241m.\u001b[39mEntry(root, width\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m50\u001b[39m)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'ttk' is not defined"
     ]
    }
   ],
   "source": [
    "input_label = ttk.Label(root, text=\"Enter a sentence:\")\n",
    "input_label.pack(pady=10)\n",
    "\n",
    "input_entry = ttk.Entry(root, width=50)\n",
    "input_entry.pack()\n",
    "\n",
    "predict_button = ttk.Button(root, text=\"Predict\", command=predict_sentiment)\n",
    "predict_button.pack(pady=10)\n",
    "\n",
    "sentiment_label = ttk.Label(root, text=\"\")\n",
    "sentiment_label.pack()\n",
    "\n",
    "sentiment_result_label = ttk.Label(root, text=\"\")\n",
    "sentiment_result_label.pack()\n",
    "# Start the Tkinter event loop\n",
    "root.mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8a010bb9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk\n",
    "from tkinter import ttk\n",
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "from sklearn.svm import SVC\n",
    "import pandas as pd\n",
    "\n",
    "# Load the sentiment analysis dataset from a CSV file\n",
    "data = pd.read_csv('sentiment_data.csv')  # Replace 'your_dataset.csv' with your actual CSV file\n",
    "\n",
    "# Preprocess text data and extract features using TF-IDF vectorization\n",
    "vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')\n",
    "X = vectorizer.fit_transform(data['text'])\n",
    "y = data['sentiment']\n",
    "\n",
    "# Train a Support Vector Machine (SVM) classifier\n",
    "svm_classifier = SVC(kernel='linear')\n",
    "svm_classifier.fit(X, y)\n",
    "\n",
    "def predict_sentiment():\n",
    "    input_text = input_entry.get()\n",
    "    if not input_text:\n",
    "        sentiment_label.config(text=\"Please enter a sentence.\")\n",
    "        return\n",
    "\n",
    "    input_vectorized = vectorizer.transform([input_text])\n",
    "    predicted_sentiment = svm_classifier.predict(input_vectorized)\n",
    "    sentiment_mapping = {'Negative': 'Negative', 'Positive': 'Positive', 'Neutral': 'Neutral'}\n",
    "\n",
    "    if predicted_sentiment[0] in sentiment_mapping:\n",
    "        predicted_sentiment_human_readable = sentiment_mapping[predicted_sentiment[0]]\n",
    "        sentiment_label.config(text=f\"Predicted Sentiment: {predicted_sentiment_human_readable}\")\n",
    "    else:\n",
    "        sentiment_label.config(text=\"Error: Unexpected sentiment prediction.\")\n",
    "\n",
    "# Create a Tkinter window\n",
    "root = tk.Tk()\n",
    "root.title(\"Sentiment Analysis\")\n",
    "\n",
    "# Create GUI elements\n",
    "input_label = ttk.Label(root, text=\"Enter a sentence:\")\n",
    "input_label.pack(pady=10)\n",
    "\n",
    "input_entry = ttk.Entry(root, width=50)\n",
    "input_entry.pack()\n",
    "\n",
    "predict_button = ttk.Button(root, text=\"Predict\", command=predict_sentiment)\n",
    "predict_button.pack(pady=10)\n",
    "\n",
    "sentiment_result_label = ttk.Label(root, text=\"\")\n",
    "sentiment_result_label.pack()\n",
    "\n",
    "# Start the Tkinter event loop\n",
    "root.mainloop()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bc2b1601",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e2676e51",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d46b4350",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "25222281",
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
