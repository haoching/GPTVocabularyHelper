# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
from os import environ
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = environ["TOKEN"]

voc = input("vocaublary")

comp = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "user", "content": "請說出接下來獎的單字繁中翻譯、詞性並用原文造句造句"},
        {"role": "user", "content": voc}
    ]
)

print(comp.choices[0].message.content)
