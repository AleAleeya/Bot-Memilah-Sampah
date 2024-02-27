import discord
from discord.ext import commands
import os
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Dan inilah cara Kamu mengganti nama file dari variabel!

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

# Membuat list sampah organik & anorganik
sampah_organik = ['daun', 'kertas', 'sisa makanan']
sampah_anorganik = ['plastik', 'kaleng', 'kabel']

@bot.command()
async def pilih_sampah(ctx):
	# Nge print sesuatu di discord
	await ctx.send("Masukkan jenis sampah: ")
	msg = await bot.wait_for("message") # Mendapatkan input dari user
	if msg.content in sampah_organik:
		await ctx.send("Masukkan ke sampah organik")
	elif msg.content in sampah_anorganik:
		await ctx.send("Masukkan ke sampah anorganik")
bot.run("TOKEN")
