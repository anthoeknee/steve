## main.py

import discord
import os
from dotenv import load_dotenv
from gpt import ask_gpt

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')  # Load Discord Token from .env
GUILD = os.getenv('DISCORD_GUILD')  # Load Discord Guild from .env

class MyClient(discord.Client): 

    async def on_ready(self):
        print(f'We have logged in as {self.user}') 
    
    async def on_message(self, message):
        if message.author == self.user:  # Ignore messages sent by bot itself
            return
        
        if message.content.startswith('!ask'):
            query = message.content[len('!ask'):].strip()  # Retrieve the query
            response = ask_gpt(query)  # Ask the question to GPT
            if response is None:  # Check if response received
                response = 'Could not get a reply from the assistant'
            await message.channel.send(response)  # Respond with the message

client = MyClient() 
client.run(TOKEN)  # Run the bot