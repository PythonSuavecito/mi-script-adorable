from telegram.ext import Updater, CommandHandler, MessageHandler, filters  # ¡'filters' en minúscula!
from telegram import Bot
import pandas as pd
from datetime import datetime
import os

TOKEN = os.getenv("TOKEN")  # Usa variables de entorno
if not TOKEN:
    print("❌ ERROR: ¿Dónde está el TOKEN, Condeso? ¡Añádelo en Render!")
    exit(1)

def start(update, context):
    update.message.reply_text("🤖 **¡BOT SINDICAL EN MODO NUBE!**\nComandos:\n/lista - Ver PDF\n/cafe - Ubicación del café")

def lista(update, context):
    try:
        update.message.reply_document(
            document=open("aniversarios_ultra_madrino.pdf", "rb"),
            caption="📜 Lista actualizada (con poderes de la nube)"
        )
    except FileNotFoundError:
        update.message.reply_text("⚠️ ¡El PDF no existe aún! Usa /generarpdf")

def cafe(update, context):
    update.message.reply_location(
        latitude=19.4326,  # Coordenadas del sindicato
        longitude=-99.1332
    )
    update.message.reply_text("☕ **¡Cafetería 'El Cortocircuito'!**\n*Pide un 'café zombie' para revivir energías* 💀⚡")

def main():
    # Configura el bot con PTB v20+
    application = Updater(TOKEN).application
    
    # Añade handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("lista", lista))
    application.add_handler(CommandHandler("cafe", cafe))
    
    print("⚡ Bot activado en la nube. ¡Viva el sindicato!")
    application.run_polling()

if __name__ == "__main__":
    main()
