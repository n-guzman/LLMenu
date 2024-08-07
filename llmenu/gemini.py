from dotenv import load_dotenv
import google.generativeai as genai
import os


load_dotenv(".env")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

with open('llmenu/system_instruction.txt', "r") as file:
    file_content = file.read()
model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=file_content)

chat = model.start_chat(history=[])

while True:
    response = chat.send_message(input('Customer: '))
    print(f'Jack: {response.text}')

    print(chat.history)