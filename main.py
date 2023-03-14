import nextcord
from nextcord.ext import commands
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
        fp = open(r'./note.md',"r+",encoding="utf-8")
        api = API(Hackmd.api_key)
        data = api.update_note(noteID,content=fp.read())
        fp.close()
class GPT:
    def Generate(vocabulary:str):
        comp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "列出"+vocabulary+"的繁中翻譯、詞性並用英文造一個句子"}
            ]
        )
        fp = open(r'./note.md',"a+",encoding="utf-8")
        fp.write(":::spoiler "+vocabulary+comp.choices[0].message.content+"\n:::\n")
        fp.close()


token = environ["BotToken"]

bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.slash_command(description="update hackmd api", guild_ids=None)
async def update(interaction: nextcord.Interaction):
    embedVar = nextcord.Embed(title="note", description="update complete", color=0x7FFFD4,url = 'https://hackmd.io/y7B_MzEoQfKAqHbhQ9GOwA?view')
    await interaction.send(embed=embedVar)
    Hackmd.update()
@bot.slash_command(description="update hackmd api", guild_ids=None)
async def add(interaction: nextcord.Interaction,vocabulary : str):
    embedVar = nextcord.Embed(title="note", description="update complete", color=0x7FFFD4,url = 'https://hackmd.io/y7B_MzEoQfKAqHbhQ9GOwA?view')
    embedVar.add_field(name="vocabulary : ", value=vocabulary, inline=False)
    await interaction.send(embed=embedVar)
    GPT.Generate(vocabulary)
    Hackmd.update()




bot.run(token)