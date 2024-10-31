import streamlit as st
from dataclasses import dataclass
import google.generativeai as genai
import os
from dotenv import load_dotenv
import json

# Load environment variables from the .env file
load_dotenv()

# Define the data structure for chat messages using a dataclass
@dataclass
class ChatMessage:
    """Represents a single chat message."""
    sender: str  # The actor who sent the message (user or assistant)
    content: str # The content of the message

# Constants for message actors
USER = "user"
ASSISTANT = "ai"
gemini_api_key = os.getenv('GOOGLE_GEMINI_API')

# Configure the Google Generative AI with the API key
genai.configure(api_key=gemini_api_key)

def format_chat(messages):
    """Format chat messages for API call."""
    chat_history = []
    for message in messages:
        chat_history.append({
            "role": "user" if message.sender == USER else "model",
            "parts": [message.content]
        })
    return chat_history

def ai_response(history):
    """
    Generate a response from the assistant based on the chat history.
    
    Args:
        history (list): The list of chat messages.
    
    Returns:
        str: The assistant's generated response.
    """
    # Read the prompt template from a file
    prompt_path = os.path.join(os.path.dirname(__file__), "prompt.txt")
    prompt = open(prompt_path, "r").read() 

    # Initialize the AI model with the specified model name and the formatted chat history
    model = genai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction=prompt)

    # Start the chat with the existing history
    chat = model.start_chat(history=format_chat(history))
    
    # Get the latest user input to send to the AI model
    latest_user_message = history[-1].content if history else ""

    # Generate the AI response based on the chat history
    response = chat.send_message(content=latest_user_message).text
    
    return response

def generate_subtasks(task: str):
    if task:
        # Add the user's message to the chat history
        st.session_state.messages.append(ChatMessage(sender=USER, content=task))

        # Display a spinner while the AI is generating a response
        with st.spinner("Generating subtasks..."):
            # Generate a response from the assistant
            assistant_response: str = ai_response(st.session_state.messages)

        # Add the assistant's response to the chat history
        st.session_state.messages.append(ChatMessage(sender=ASSISTANT, content=assistant_response))

        # Return subtasks
        try:
            subtasks = json.loads(assistant_response)
            if not subtasks:
                raise ValueError("Subtasks cannot be empty")
            if not isinstance(subtasks, list):
                raise ValueError("Subtasks should be a list")
            return subtasks
        except (json.JSONDecodeError, ValueError):
            st.error("Failed to generate subtasks. Please try again.")
            return []