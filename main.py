from telegram.ext import Application, CommandHandler
from telegram.error import Conflict
import os
import logging

# Configura logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("TOKEN")

async def start(update, context):
    await update.message.reply_text("🤖 ¡Bot activado con poderes anti-conflicto!")

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    
    try:
        # ¡Clave! drop_pending_updates y manejo de errores
        application.run_polling(
            drop_pending_updates=True,
            close_loop=False,
            stop_signals=None
        )
    except Conflict as e:
        logger.error(f"🚨 Error de conflicto: {e}")
        logger.info("Reiniciando el bot en 5 segundos...")
        time.sleep(5)
        main()  # Reinicio automático

if __name__ == "__main__":
    main()
