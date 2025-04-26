from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram import Bot
import os

TOKEN = os.getenv("TOKEN")
if not TOKEN:
    print("❌ ERROR: ¡Token no encontrado! Añádelo en Render.")
    exit(1)

async def start(update, context):
    await update.message.reply_text("🤖 **¡BOT SINDICAL ACTIVADO!**\nComandos:\n/lista - Ver PDF\n/cafe - Ubicación del café")

async def lista(update, context):
    try:
        await update.message.reply_document(
            document=open("aniversarios_ultra_madrino.pdf", "rb"),
            caption="📜 Lista actualizada"
        )
    except FileNotFoundError:
        await update.message.reply_text("⚠️ ¡El PDF no existe! Usa /generarpdf")

async def cafe(update, context):
    await update.message.reply_location(
        latitude=19.4326,
        longitude=-99.1332
    )
    await update.message.reply_text("☕ **¡Cafetería 'El Cortocircuito'!**")

def main():
    # Configuración correcta para PTB v20+
    application = Application.builder().token(TOKEN).build()
    
    # Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("lista", lista))
    application.add_handler(CommandHandler("cafe", cafe))
    
    print("⚡ Bot activado en la nube. ¡Viva el sindicato!")
    application.run_polling()

if __name__ == "__main__":
    main()
