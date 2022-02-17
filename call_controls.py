
from time import sleep, strftime, localtime, time
from winsound import MB_OK
from telegram import ForceReply, Update
from telegram.ext import  CallbackContext
from mabot import TIME_OLD_STOP_RECORD, TIME_NEW_STOP_RECORD
from env import BOT_TOKEN
import telegram
import pyautogui as pa
import Security as Sec
import utilities as ut
import ctypes
import os


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def tragas_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /pene is issued."""
    update.message.reply_text('Tragas!')

def shelly_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /shelly is issued."""
    global TIME_NEW_STOP_RECORD
    global TIME_OLD_STOP_RECORD
    #print(strftime('%Y-%m-%d %H:%M:%S', localtime()))
    TIME_NEW_STOP_RECORD = time()
    if ut.checkShortTime(TIME_OLD_STOP_RECORD, TIME_NEW_STOP_RECORD) == True:
        TIME_OLD_STOP_RECORD = TIME_NEW_STOP_RECORD
        update.message.reply_text('Peciosa! Less than 10 s')
    else:
        TIME_OLD_STOP_RECORD = TIME_NEW_STOP_RECORD
        update.message.reply_text('dambembe! More than 10s')

def ya_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /ya is issued."""
    pa.hotkey('alt', 'shift', 'a')
    sleep(3)
    pa.hotkey('win', '5')
    sleep(3)
    pa.hotkey('alt','shift', 'S')
    update.message.reply_text('Oks! Well send the video')


def fin_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /fin is issued."""
    pa.hotkey('alt', 'shift', 'a')
    sleep(3)
    pa.hotkey('win', '5')
    sleep(3)
    pa.hotkey('alt','shift', 'S')
    update.message.reply_text('Okasss!')
    chat_id = update.message.chat_id
    bot = telegram.Bot(token=BOT_TOKEN)
    bot.sendVideo(chat_id = chat_id, video = open(RECORDS_DIR +'\\'+  os.listdir(RECORDS_DIR)[len(os.listdir(RECORDS_DIR))-1], 'rb'))
    #messagebox.showinfo("Telegram bot", "Video sent")
    ut.theNotitifacion("Telegram bot", "Recording sent")
    update.message.reply_text('Video sent')

def restart_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /restart is issued."""
    chat_id = update.message.chat_id
    if Sec.CheckingRath(update, chat_id) == True:
        pa.hotkey('alt', 'ctrl', 's')
        sleep(3)
        pa.hotkey('win', '1')
        sleep(3)
        pa.hotkey('alt','shift', 'q')
        sleep(3)
        pa.hotkey('ctrl','e')
        sleep(1)
        pa.hotkey('ctrl','d')
        update.message.reply_text('Ay no')

def img_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /shot is issued."""
    chat_id = update.message.chat_id
    if Sec.CheckingRath(update, chat_id) == True:
        pa.screenshot('ma_screenshot.png')
        bot = telegram.Bot(token=BOT_TOKEN)
        bot.sendPhoto(chat_id = chat_id, photo = open('ma_screenshot.png', 'rb'))
        #bot.sendPhoto(chat_id = chat_id, photo = open(WALLPAPER_DIR +'\\'+  os.listdir(WALLPAPER_DIR)[len(os.listdir(WALLPAPER_DIR))-1], 'rb'))
        ut.theNotitifacion("Telegram bot", "Image sent")
        ctypes.windll.user32.MessageBoxA(None, "S","T", 0x1000| MB_OK | ICON_INFO)
        update.message.reply_text('Image sent')

def sendRecording_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /record is issued."""
    chat_id = update.message.chat_id
    if Sec.CheckingRath(update, chat_id) == True:
        bot = telegram.Bot(token=BOT_TOKEN)
        acces_recors_dir = os.listdir(RECORDS_DIR)
        bot.sendVideo(chat_id = chat_id, video = open(RECORDS_DIR +'\\'+  acces_recors_dir[len(acces_recors_dir)-1], 'rb'))
        ut.theNotitifacion("Telegram bot", "Recording sent")
        ctypes.windll.user32.MessageBoxA(None, "S","T", 0x1000| MB_OK | ICON_INFO)
        update.message.reply_text('Video sent')

def mute_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /mute is issued."""
    chat_id = update.message.chat_id
    if Sec.CheckingRath(update, chat_id) == True:
        pa.hotkey('ctrl', 'd')
        sleep(0.5)
        pa.screenshot('ma_screenshot.png')
        bot = telegram.Bot(token=BOT_TOKEN)
        bot.sendPhoto(chat_id = chat_id, photo = open('ma_screenshot.png', 'rb'))
    

MB_OK = 0x0
MB_OKCXL = 0x01
MB_YESNOCXL = 0x03
MB_YESNO = 0x04
MB_HELP = 0x4000
ICON_EXLAIM=0x30
ICON_INFO = 0x40
ICON_STOP = 0x10
WALLPAPER_DIR = 'D:\\Rath\\wallpapers'
RECORDS_DIR = 'D:\\Rath\\Univesity\\Record temps'
