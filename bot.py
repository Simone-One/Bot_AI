import discord
from discord.ext import commands
from ai import rileva_dispositivo

# definiamo i permessi di discord
intents = discord.Intents.default()
intents.message_content = True

# creo il bot
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Il bot {bot.user} è online")

@bot.command()
async def test(ctx):
    await ctx.send("Test OK")

@bot.command()
async def check(ctx):
    # recupero gli eventuali allegati a un messaggio
    allegati = ctx.message.attachments
    for allegato in allegati:
        # ciclo ogni allegato per salvare ogni allegato nel pc
        nome_file = allegato.filename
        # recuperiamo l'url del file salvato nei server di discord
        file_url = allegato.url
        # salvo l'allegato
        await allegato.save(f"img/{nome_file}")
        # chiameremo il modello AI addestrato che farà interferenza (usare il modello addestrato per fare una previsione)
        classe, punteggio = rileva_dispositivo("keras_model.h5", "labels.txt", f"img/{nome_file}")
        await ctx.send(f"L'immagine che mi hai inviato è un {classe}")

bot.run("TOKEN")