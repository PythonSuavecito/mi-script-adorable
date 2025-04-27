from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram import Bot, Update
import os
import logging

# Configura logging para ver errores
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("TOKEN")
if not TOKEN:
    logger.error("❌ ¡TOKEN no encontrado! Añádelo en Render como variable de entorno.")
    exit(1)

# ---- COMANDOS CON ACTITUD ----
async def start(update: Update, context) -> None:
    await update.message.reply_text(
        "⚡ *¡BOT SINDICAL EN LÍNEA!* ⚡\n"
        "Comandos:\n"
        "/lista - Ver PDF de aniversarios\n"
        "/cafe - Ubicación de *'El Cortocircuito'* (donde los muertos vivientes toman café)\n"
        "/meme - ¿Un meme sindical? ¡Claro!",
        parse_mode="Markdown"
    )

async def cafe(update: Update, context) -> None:
    await update.message.reply_location(
        latitude=19.4326,  # Coordenadas del legendario café
        longitude=-99.1332
    )
    await update.message.reply_text(
        "☕ *¡CAFETERÍA «EL CORTOCIRCUITO»!*\n"
        "_Especialidad:_ Café con chispas de transformador quemado.\n"
        "⚠️ *Horario:* Siempre abierto (como tu bot en Render).",
        parse_mode="Markdown"
    )

# ---- CONFIGURACIÓN DEL BOT ----
def main() -> None:
    application = Application.builder().token(TOKEN).build()
    
    # Añade handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("cafe", cafe))
    
    # Log para confirmar que el bot arrancó
    logger.info("🤖 Bot activado. ¡A revivir compañeros como zombies!")
    application.run_polling()

if __name__ == "__main__":
    main()
