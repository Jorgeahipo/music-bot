import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Token de tu bot
TOKEN = "8516600387:AAGk3lELHrX_-wljbmorz8ejWtucPZLMQkc"

# Configurar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('🎵 ¡Hola! Soy tu bot de música. ¡Funciono 24/7 en la nube!')

async def agregar(update: Update, context: CallbackContext):
    if context.args:
        cancion = ' '.join(context.args)
        await update.message.reply_text(f'✅ Canción agregada: {cancion}')
    else:
        await update.message.reply_text('Usa: /agregar nombre de la canción')

def main():
    # Crear aplicación
    app = Application.builder().token(TOKEN).build()
    
    # Comandos
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("agregar", agregar))
    
    # Iniciar bot
    logger.info("Bot iniciado en la nube 🚀")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()