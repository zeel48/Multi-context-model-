from pyexpat import model
import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Function to perform sentiment analysis and update GUI
def analyze_sentiment():
    text = text_entry.get("1.0", "end-1c").strip()  # Get text from text entry
    if not text:
        messagebox.showwarning("Warning", "Please enter text to analyze.")
        return
    
    # Vectorize the input text using the pre-fitted vectorizer
    text_vectorized = np.vectorize.transform([text])
    
    # Predict sentiment
    sentiment = model.predict(text_vectorized)[0]
    sentiment_label.config(text=f"Sentiment: {'Positive' if sentiment == 1 else 'Negative'}")

# Create the main application window
root = tk.Tk()
root.title("IMDB Sentiment Analysis")

# Create GUI elements
label = tk.Label(root, text="Enter movie review to analyze:")
label.pack(pady=10)

text_entry = tk.Text(root, height=10, width=50)
text_entry.pack()

analyze_button = tk.Button(root, text="Analyze Sentiment", command=analyze_sentiment)
analyze_button.pack(pady=10)

sentiment_label = tk.Label(root, text="Sentiment: ")
sentiment_label.pack()

# Run the main loop
root.mainloop()
