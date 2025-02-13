import streamlit as st
import nltk  # For working with text
from nltk.corpus import stopwords  # For removing common words
from nltk.tokenize import word_tokenize
import os
import groq  # Groq API for Llama 3.0
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Download NLTK data (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')

# Initialize Groq API client
                                       # Replace with your Groq API key
client = groq.Client(api_key=os.getenv('GROQ_KEY'))

# Function to interact with Llama 3.0 via Groq API
def generate_with_groq(prompt):
    #try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # Use Llama 3.0 model
            messages=[{"role": "user", "content": prompt}],  # Proper format for chat models
            max_tokens=500,  # Limit the response length
            temperature=0.7,  # Adjust creativity of the response
        )
        return response.choices[0].message.content.strip()
        #return response.choices[0].text.strip()
    #except Exception as e:
        #return f"Error generating response: {str(e)}"

# Health bot logic
def health_bot(user_input):
    if "symptom" in user_input:
        return "Please consult a doctor for accurate advice."
    elif "appointment" in user_input:
        return "Would you like to schedule an appointment with the doctor?"
    elif "medication" in user_input:
        return "I would suggest you, but it's important to take prescribed medicine by a doctor."
    else:
        # Use Groq API to generate a response
        response = generate_with_groq(user_input)
        return response

# Streamlit web application
def main():
    st.title("AI Chatbot for Health")
    user_input = st.text_input("What's your problem?")
    if st.button('SUBMIT'):
        if user_input:
            st.write("Concern:", user_input)
            with st.spinner("Processing your queries... Please wait"):
                response = health_bot(user_input)
            st.write("Solution by me:", response)
        else:
            st.write("Please enter your concern???")

# Run the app
if __name__ == "__main__":
    main()