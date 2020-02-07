from .__utils import bot, MAIN_ACTIVITY_FLAG, MERCH_ACTIVITY_FLAG, DISPLAY_MERCH
from .__fillers import MerchMessageFiller
from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from bot.models import Merch




message_filler = MerchMessageFiller()




def start_merch_activity(update, context):
    print('---------------------------------------------------------------------')
    print('merch. start merch activity\n')

    chat_id = context.chat_data.get('chat_id')

    merches = Merch.objects.all()

    keyboard = []

    for merch in merches:
        keyboard.append([InlineKeyboardButton(merch.name, callback_data=DISPLAY_MERCH + ' ' + str(merch.pk))])

    inline_markup = InlineKeyboardMarkup(keyboard)

    message = message_filler.merch_start_message

    context.chat_data['message_id'] = bot.send_message(chat_id=chat_id, text=message, reply_markup=inline_markup).message_id

    return MERCH_ACTIVITY_FLAG


def display_merch(update, context):
    print('---------------------------------------------------------------------')
    print('merch. display merch\n')

    chat_id = context.chat_data.get('chat_id')
    message_id = context.chat_data.get('message_id')

    bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id)

    merch_pk = int(update.callback_query.data.split(' ')[1])

    merch = Merch.objects.get(pk=merch_pk)

    images = merch.images.all()

    images_inputs = []

    for image in images:
        print(image.image_file.url)

        images_inputs.append(InputMediaPhoto(open(image.image_file.path, 'rb')))

    images_inputs[0].caption = merch.description
    
    bot.send_media_group(chat_id=chat_id, media=images_inputs)

    return MAIN_ACTIVITY_FLAG