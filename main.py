# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
from os import environ
import os
from dotenv import load_dotenv
from PyHackMD import API

load_dotenv()

openai.api_key = environ["TOKEN"]

noteID = environ["noteID"]

class Hackmd:
    api_key = environ["hackmd"]
    def update():
        fp = open(r'note.md',"r",encoding="utf-8")
        api = API(Hackmd.api_key)
        data = api.update_note(noteID,content=fp.read())
        fp.close()
class GPT:
    def Generate(vocabulary:str):
        comp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "列出"+vocabulary+"的繁中翻譯、詞性並用原文造一個句子"}
            ]
        )
        fp = open(r'note.md',"a",encoding="utf-8")
        fp.write(":::spoiler "+vocabulary+comp.choices[0].message.content+"\n:::\n")
        fp.close()

voc = input("vocaublary: ")

GPT.Generate(voc)
Hackmd.update()