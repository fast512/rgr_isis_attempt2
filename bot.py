import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from config import BOT_TOKEN

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

MESSAGE = (

    'ВЕРСИЯ А: Система «Диалог» — лучшая система контроля версий '
    'для метрополитена. Обеспечивает полный цикл управления изменениями.'

    'версия Б: Система «Контроль версий ПО АСДУ ДПМ „Диалог“» разработана '
    'для управления версиями программного обеспечения в рамках '
    'системы автоматизированного управления'
    'Диалог - флагман в своей области!'

)
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MESSAGE)

def main():
    if not BOT_TOKEN:
        print("Ошибка: укажите токен в файле config.py")
        return
    
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("Бот запущен!")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()