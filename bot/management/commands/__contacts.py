from .__fillers import ContactsMessageFiller
from .__utils import bot, MAIN_ACTIVITY_FLAG




message_filler = ContactsMessageFiller()




def start_contacts_activity(update, context):
    print('---------------------------------------------------------------------')
    print('contacts. send contacts\n')

    contacts = message_filler.contacts_message

    chat_id = context.chat_data.get('chat_id')

    bot.send_message(chat_id=chat_id, text=contacts)

    return MAIN_ACTIVITY_FLAG