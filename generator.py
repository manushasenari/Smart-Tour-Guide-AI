import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure the Gemini API with the API key
genai.configure(api_key=api_key)

# Initialize the generative model
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to get a response from the Gemini model for any user question
def get_reply(user_question, topic="General Travel"):
    # Create a prompt with travel context
    prompt = f"""
    You are a Smart Tour Guide, an expert in travel planning and recommendations.
    The user has asked a question related to the topic: {topic}.
    Provide a detailed, helpful, and accurate response to the following question:
    Question: {user_question}
    If the question is vague or off-topic, politely clarify and provide a relevant travel-related answer.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"