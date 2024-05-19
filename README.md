**College Enquiry AI Chatbot**

**Overview**

Welcome to the College Enquiry AI Chatbot repository! This project features an AI-powered chatbot designed to assist users with inquiries about college-related information. Leveraging natural language processing and machine learning, the chatbot can handle various questions related to courses, admissions, fees, and more. The project includes a user-friendly GUI built with Tkinter for seamless interaction.

**Features**

**1. Natural Language Processing:** Utilizes NLP techniques to understand and process user queries.

**2. Contextual Responses:** Provides relevant responses based on predefined intents and patterns.

**3. GUI Integration:** Offers a graphical user interface using Tkinter for easy interaction.

**4. Machine Learning Model:** Employs a trained neural network model for intent classification and response generation.

**5. Extensive College Information:** Covers a wide range of college-related topics, from courses to facilities.




**Technologies Used**

**1. Programming Language:** Python

**2. Machine Learning Framework:** TensorFlow

**3. NLP Libraries:** NLTK

**4. GUI Framework:** Tkinter

**5. Data Storage:** JSON, Pickle



**Project Structure**

**1. intents.json:** Contains predefined intents, patterns, and responses for the chatbot.

**2. chatbotmodel.h5:** The trained neural network model for intent classification.

**3. words.pkl and classes.pkl:** Pickle files storing the vocabulary and class labels.

**4. main.py:** Main Python script to run the chatbot application.


**Getting Started**
**Prerequisites**
- Python 3.7 or higher
- pip (Python package installer)

**Installation**

**1. Clone the repository:**
git clone https://github.com/yourusername/college-enquiry-chatbot.git
cd college-enquiry-chatbot


**2. Create and activate a virtual environment:**
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`


**3. Install dependencies:**
pip install -r requirements.txt



**Running the Chatbot**

**1. Download NLTK data:**
import nltk
nltk.download('punkt')
nltk.download('wordnet')


**2. Start the chatbot:**
python main.py


**3. Interact with the chatbot:**
Open the Tkinter GUI that launches with the script and start typing your queries.


**Usage**

The chatbot can handle a variety of inquiries related to college information, such as:

**1. Greetings:** "Hello", "Hi"

**2. Course details:** "What courses are available?"

**3. Admission requirements:** "What are the student requirements for admission?"

**4. Fees:** "How much is the college fee?"

**5. Locations:** "Where is the college located?"


**Example Interaction**

**User:** What courses are available?

**Bot:** Bharti Vidyapeeth(Deemed to be University), Pune (India), offers BSc (Hons) Computing, BBA (Marketing) with International Business, and more.


**Contributing**
We welcome contributions to enhance the functionality and usability of the AI Chatbot. Please follow these steps to contribute:
1. Fork the repository
2. Create a new branch (git checkout -b feature/your-feature)
3. Commit your changes (git commit -m 'Add some feature')
4. Push to the branch (git push origin feature/your-feature)
5. Open a Pull Request

**License**
This project is licensed under the MIT License. See the LICENSE file for details.

**Acknowledgements**
1. NLTK
2. TensorFlow
3. Tkinter
