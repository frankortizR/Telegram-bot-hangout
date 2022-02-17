from time import time
from plyer import notification

def theNotitifacion(the_title, the_message):
    notification.notify(
                title = the_title,
                message = the_message,
                app_icon = "C:\\Users\\Frank\\Desktop\\Frank\\Projects\\Mines\\Python\\Telegram_bots\\Test1\\icon2.ico",
                timeout = 6800
        )

def checkShortTime(time_1, time_2):
    time_interval = time_2 - time_1
    if (time_interval) < 10:
        return True
    else:
        return False