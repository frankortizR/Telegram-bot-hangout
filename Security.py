
def CheckingRath(update, chat_id):
    if chat_id != 1144214477:
        update.message.reply_text('No access allowed!')
        return False
    else:
        return True