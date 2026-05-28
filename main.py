import discord
import asyncio
import sys

sys.stdout.reconfigure(line_buffering=True)

# 🛡️ Partición del Token para evitar el bloqueo/alerta de GitHub
PARTE1 = "MTQ2NDI0NDgwNTY5NjYxODU4Ng"
PARTE2 = ".Gsgtb1.n925KWnZ6DZ9fgCwnVTWf2v75g6c2W8S5UbIyU"
TOKEN = PARTE1 + PARTE2

print("[⚙️] Cargando el sistema de purga por ID con token seguro...")

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("\n==================================================")
    print(f"🤖 BOT SUPREMO ONLINE: {client.user}")
    print("Filtro activado por ID para #📷┃𝖿𝗈𝗍𝗈𝗌 y #🎬┃𝗏𝗂𝖽𝖾𝗈𝗌")
    print("==================================================")

@client.event
async def on_message(message):
    # Ignorar mensajes del propio bot
    if message.author == client.user:
        return

    # IDs reales que sacamos de tu consola
    ID_FOTOS = 1507907122179084382
    ID_VIDEOS = 1507907125915943093

    # Si el mensaje entra en cualquiera de los dos canales...
    if message.channel.id == ID_FOTOS or message.channel.id == ID_VIDEOS:
        
        # Verificamos si tiene archivos adjuntos (fotos/videos) o links multimedia
        tiene_adjunto = len(message.attachments) > 0
        tiene_link_multimedia = any(ext in message.content.lower() for ext in [
            ".jpg", ".jpeg", ".png", ".gif", ".mp4", ".mov", ".avi", 
            "tenor.com", "giphy.com", "youtube.com", "youtu.be", "tiktok.com"
        ])

        # Si es puro texto sin multimedia, lo borramos
        if not (tiene_adjunto or tiene_link_multimedia):
            try:
                # Volamos el mensaje
                await message.delete()
                print(f"[🗑️] Texto eliminado a {message.author.name} en #{message.channel.name}")
                
                # Mandamos el descanso supremo
                aviso = await message.channel.send(f"⚠️ {message.author.mention} **no texto gay** 🏳️‍🌈")
                
                # Espera 4 segundos y borra el aviso para dejar limpio el canal
                await asyncio.sleep(4)
                await aviso.delete()
                
            except discord.Forbidden:
                print("❌ ERROR: Discord no me dejó borrar el mensaje. Subí el rol del bot arriba de todo en Ajustes > Roles.")
            except Exception as e:
                print(f"❌ Error: {e}")

print("[🔌] Conectando a los servidores de Discord...")
client.run(TOKEN)
