from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram import Update
import pandas as pd
import os
import logging

# Configura logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("TOKEN")
CSV_PATH = "lista_aniversarios.csv"

# ---- COMANDOS PODEROSOS ----
async def start(update: Update, context):
    await update.message.reply_text(
        "⚡ *¡BOT SINDICAL 2.0!* ⚡\n"
        "Comandos:\n"
        "/agregar <No.> <Nombre> <Años> - Añade un compañero\n"
        "/revivir <Nombre> - Resucita a un zombie sindical\n"
        "/lista - Muestra el PDF de aniversarios\n"
        "/cafe - Ubicación del *Cortocircuito*",
        parse_mode="Markdown"
    )

async def agregar(update: Update, context):
    try:
        _, numero, nombre, anios = update.message.text.split(maxsplit=3)
        df = pd.read_csv(CSV_PATH, encoding='latin1')
        nuevo_registro = {"No.": numero, "NOMBRE": nombre, "ANIVERSARIO": f"{anios} AÑOS"}
        df = pd.concat([df, pd.DataFrame([nuevo_registro])], ignore_index=True)
        df.to_csv(CSV_PATH, index=False)
        await update.message.reply_text(f"✅ *{nombre}* añadido. ¡A festejar {anios} años!")
    except Exception as e:
        await update.message.reply_text(f"❌ Error: Usa /agregar <No.> <Nombre> <Años>")

async def revivir(update: Update, context):
    nombre = update.message.text.split(maxsplit=1)[1]
    await update.message.reply_text(
        f"☠️ *{nombre} HA RESUCITADO* ¡Bienvenido al sindicato zombie!",
        parse_mode="Markdown"
    )

# ---- CONFIGURACIÓN ----
def main():
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("agregar", agregar))
    application.add_handler(CommandHandler("revivir", revivir))
    
    logger.info("🤖 Bot activado. ¡A chambear!")
    application.run_polling()

if __name__ == "__main__":
    main()
