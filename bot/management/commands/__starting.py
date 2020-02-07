from telegram import Bot, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from .__fillers import StartKeyboardFiller, StartMessageFiller
from bot.models import User
from .__utils import bot, REGISTRATION_ACTIVITY_FLAG, REGISTRATION_YEAR, MAIN_ACTIVITY_FLAG

message_filler = StartMessageFiller()
keyboard_filler = StartKeyboardFiller()




def initialize_main_keyboard():
    keyboard = keyboard_filler.main_menu_keyboard

    return ReplyKeyboardMarkup(keyboard)


def start(update, context):
    print('---------------------------------------------------------------------')
    print('start\n')

    user_id = update.message.from_user.id
    chat_id = update.message.chat.id

    user_first_name = update.message.from_user.first_name
    user_last_name = update.message.from_user.last_name

    telegram_full_name = f'{user_first_name} {user_last_name}' if user_last_name != None else user_first_name

    telegram_username = update.message.from_user.username

    context.chat_data['user_id'] = user_id
    context.chat_data['chat_id'] = chat_id

    (user, isUserNew) = User.objects.get_or_create(telegram_id=user_id,
                                      defaults={
                                                'telegram_name': telegram_full_name,
                                                'telegram_username': telegram_username,
                                                'group': None,
                                                'spec': None})

    if not isUserNew:
        user.telegram_name = telegram_full_name
        user.telegram_username = telegram_username
        user.save()

    print(f'telegram id: {user_id}\n')
    print(f'db id: {user.telegram_id}\nNew user: {isUserNew}\n')

    bot.send_message(chat_id=chat_id, text=message_filler.start_hello_message)

    if(isUserNew):
        keyboard = keyboard_filler.registration_offer_keyboard

        button = [[InlineKeyboardButton(keyboard[0][0], callback_data=REGISTRATION_YEAR)]]

        inline_markup = InlineKeyboardMarkup(button)

        message = bot.send_message(chat_id=chat_id, text=message_filler.new_user_start_ending_message, 
                         reply_markup=inline_markup)

        context.chat_data['message_id'] = message.message_id

        return REGISTRATION_ACTIVITY_FLAG
    else:
        reply_markup = initialize_main_keyboard()

        bot.send_message(chat_id=chat_id, text=message_filler.old_user_start_ending_message, reply_markup=reply_markup)

    return MAIN_ACTIVITY_FLAG