import discord
import os
from discord.ext import commands
from logic import api
from config import TOKEN

# Inisialisasi bot
intents = discord.Intents.default()
intents.message_content = True  # Diperlukan untuk mendapatkan konten pesan
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_message(message):
    # kalau yg kirim chat adalah user --> chat akan dianggap sebagai prompt
    # kalau yang kirim chat adalah bot --> akan diabaikan
    if message.author == bot.user:
        return 
    
    prompt = message.content

    file_path = api.download_image(prompt)

    with open(file_path, "rb") as photo:
        await message.channel.send(file=discord.File(photo, 'generated_image.jpg'))

    os.remove(file_path)

bot.run(TOKEN)
