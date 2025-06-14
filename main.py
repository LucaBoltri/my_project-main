import discord
from discord.ext import commands
from clasificador import indentificador


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def demo(ctx):
    if ctx.message.attachments:
        for imagen in ctx.message.attachments:
            nombre_imagen = imagen.filename
            url_imagen = imagen.url
            await imagen.save(f'image/{nombre_imagen}')
            await ctx.send(indentificador(f'image/{nombre_imagen}'))
            await ctx.send('imagen guardada correctamente')
    else:
        await ctx.send("No has adjuntado una imagen.")


bot.run("tu token de discord")
