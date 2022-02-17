#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
from multiprocessing import context
from turtle import update
import call_controls as cc
import logging
import telegram
from telegram import Update, Bot, bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

    
#============================================================================================---->
#============================================================================================---->
def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    
    update.message.reply_text(update.message.text)

def tragas(update: Update, context: CallbackContext) -> None:
    print(update.message.text.upper().find("PENE"))
    if(update.message.text.upper().find("PENE") >= 0):
        update.message.reply_text("Tragas")


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("5217446941:AAH9hPdccRpnjE__BmeCeTVUOip98_gfCS4")
    bot = telegram.Bot(token="5217446941:AAH9hPdccRpnjE__BmeCeTVUOip98_gfCS4")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", cc.start))
    dispatcher.add_handler(CommandHandler("help", cc.help_command))
    dispatcher.add_handler(CommandHandler("pene", cc.tragas_command))
    dispatcher.add_handler(CommandHandler("shelly", cc.shelly_command))
    dispatcher.add_handler(CommandHandler("ya", cc.ya_command))
    dispatcher.add_handler(CommandHandler("fin", cc.fin_command))
    dispatcher.add_handler(CommandHandler("restart", cc.restart_command))
    dispatcher.add_handler(CommandHandler("img", cc.img_command))
    dispatcher.add_handler(CommandHandler("record", cc.sendRecording_command))
    dispatcher.add_handler(CommandHandler("mute", cc.mute_command))
    

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, tragas))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


TIME_OLD_STOP_RECORD = 0.0
TIME_NEW_STOP_RECORD = 0.0
if __name__ == '__main__':
    main()