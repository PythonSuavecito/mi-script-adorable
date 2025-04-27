from telegram.ext import Application, CommandHandler
import os
import logging
import asyncio

# Configura logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("TOKEN")

async def start(update, context):
    await update.message.reply_text("⚡ ¡Bot activado correctamente en Render! ⚡")

def run_bot():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    
    # Configuración especial para evitar cierres
    application.run_polling(
        drop_pending_updates=True,
        close_loop=False,  # Evita que se cierre el loop
        stop_signals=None  # Ignora señales de terminación
    )

if __name__ == "__main__":
    # Fuerza comportamiento continuo
    while True:
        try:
            logger.info("Iniciando bot...")
            run_bot()
        except Exception as e:
            logger.error(f"Error: {e}. Reiniciando en 5 segundos...")
            asyncio.run(asyncio.sleep(5))
