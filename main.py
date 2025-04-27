from telegram.ext import Application, CommandHandler
from telegram.error import Conflict
import os
import logging
import time  # Para el reinicio automático

# Configura logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("TOKEN")

async def start(update, context):
    await update.message.reply_text("⚡ ¡Bot sindical activado! ⚡")

def run_bot():
    """Función que crea y ejecuta el bot"""
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    
    try:
        # Configuración para Render (puerto obligatorio)
        PORT = int(os.environ.get('PORT', 10000))
        logger.info(f"🚀 Iniciando bot en puerto {PORT}...")
        
        application.run_polling(
            drop_pending_updates=True,
            close_loop=False,
            port=PORT  # ¡Clave para Render!
        )
    except Conflict as e:
        logger.error(f"🔴 Error: {e}. Reiniciando en 5 segundos...")
        time.sleep(5)
        run_bot()  # Reinicio automático

if __name__ == "__main__":
    run_bot()  # ¡Aquí se ejecuta todo!
