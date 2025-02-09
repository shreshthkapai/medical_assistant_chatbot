from main import chat
import gradio as gr

gr.ChatInterface(fn = chat, type = "messages").launch(share = True)