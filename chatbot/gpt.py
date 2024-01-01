## gpt.py

import openai
import os

# load your OpenAI secret key from .env file
openai.api_key = os.getenv("OPENAI_KEY")

def ask_gpt(query):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=query,
            temperature=0.6,
            max_tokens=150
        )
        
        return response.choices[0].text.strip()

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return None