from env import MY_CHAT_ID

def CheckingRath(update, chat_id):
    if chat_id != MY_CHAT_ID:
        update.message.reply_text('No access allowed!')
        return False
    else:
        return True