import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

if openai_api_key:
    print("OpenAI API Key loaded succesully")
else:
    print("Unable to load OpenAI API Key.")

openai = OpenAI()
MODEL = 'gpt-4o-mini'

system_message = """You are a helpful medical assistant that helps patients with 
their health concerns and queries. Dont go too off-topic from the medical domain."""

def chat(message, history):
    messages = ([{"role": "system", "content": system_message}] + 
                history 
                + [{"role": "user", "content": message}])

    stream = openai.chat.completions.create(model=MODEL, messages=messages, stream=True)

    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ''
        yield response




