import random
import json
import pickle
import numpy as np
import tkinter as tk
from tkinter import scrolledtext, END
import nltk
from nltk.stem import WordNetLemmatizer
import tensorflow as tf
from tensorflow.keras.models import load_model

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

intents = json.loads(open('intents.json').read())

with open('words.pkl', 'rb') as f:
    words = pickle.load(f)

with open('classes.pkl', 'rb') as f:
    classes = pickle.load(f)

model = load_model('chatbotmodel.h5')

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = [{'intent': classes[r[0]], 'probability': str(r[1])} for r in results]
    return return_list

def get_response(intents_list, intents_json):
    if intents_list:
        tag = intents_list[0]['intent']
        list_of_intents = intents_json['intents']
        for intent in list_of_intents:
            if intent['tag'] == tag:
                result = random.choice(intent['responses'])
                return result
    else:
        return "Sorry, I'm not sure how to respond to that."

def send(event=None):  # Accept an event argument to handle <Return> event binding
    message = entry.get()
    entry.delete(0, END)
    if message.lower() == "bye" or message.lower() == "goodbye":
        ints = predict_class(message)
        res = get_response(ints, intents)
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, "You: " + message + "\n")
        chat_box.insert(tk.END, "Bot: " + res + "\n")
        chat_box.config(state=tk.DISABLED)
        chat_box.see(tk.END)
        chat_box.insert(tk.END, "The Program Ends here!\n")
    else:
        ints = predict_class(message)
        res = get_response(ints, intents)
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, "You: " + message + "\n")
        chat_box.insert(tk.END, "Bot: " + res + "\n")
        chat_box.config(state=tk.DISABLED)
        chat_box.see(tk.END)

def clear_all():
    entry.delete(0, END)
    chat_box.config(state=tk.NORMAL)
    chat_box.delete(1.0, END)
    chat_box.config(state=tk.DISABLED)

# GUI
root = tk.Tk()
root.title("College Enquiry Chatbot")

frame = tk.Frame(root)
frame.pack(pady=10)

# Add "Enter: " label before the entry field
tk.Label(frame, text="Enter: ").grid(row=1, column=1)

chat_box = scrolledtext.ScrolledText(frame, width=80, height=20)
chat_box.grid(row=1, column=0, padx=5, pady=5, columnspan=2, sticky='nsew')
chat_box.config(state=tk.DISABLED)

# Add another empty label for spacing above the entry field
tk.Label(frame, text="").grid(row=2, column=0)

entry = tk.Entry(frame, width=40)
entry.grid(row=3, column=0, padx=5, pady=5, sticky='ew')
entry.bind('<Return>', send)  # Bind the send function to the <Return> event

send_button = tk.Button(frame, text="Send", width=10, command=send)
send_button.grid(row=3, column=1, padx=5, pady=5, sticky='ew')

clear_button = tk.Button(frame, text="Clear All", width=10, command=clear_all)
clear_button.grid(row=4, column=0, pady=5, padx=5, sticky='ew')

# Configure resizing behavior
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)

root.mainloop()

