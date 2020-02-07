
from .__utils import bot, MAIN_ACTIVITY_FLAG, PROFILE_ACTIVITY_FLAG, REGISTRATION_YEAR, REGISTRATION_ACTIVITY_FLAG
from .__utils import PROFILE, REREGISTRATION
from .__fillers import ProfileMessageFiller, ProfileKeyboardFiller
from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton
from bot.models import User




message_filler = ProfileMessageFiller()
keyboard_filler = ProfileKeyboardFiller()




def start_profile_activity(update, context):
    print('---------------------------------------------------------------------')
    print('profile. start profile activity\n')

    chat_id = context.chat_data.get('chat_id')

    start_message = message_filler.start_message

    profile = keyboard_filler.profile_button_text
    reregistration = keyboard_filler.reregistration_button_text

    keyboard = [[InlineKeyboardButton(profile, callback_data=PROFILE)],
                [InlineKeyboardButton(reregistration, callback_data=REREGISTRATION)]]

    inline_markup = InlineKeyboardMarkup(keyboard)

    context.chat_data['message_id'] = bot.send_message(chat_id=chat_id, text = start_message,
                                                       reply_markup=inline_markup).message_id

    return PROFILE_ACTIVITY_FLAG


def start_registration(update, context):
    print('---------------------------------------------------------------------')
    print('profile. start reregistration\n')

    chat_id = context.chat_data.get('chat_id')
    message_id = context.chat_data.get('message_id')

    bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id)

    reregistration_message = message_filler.reregistration_message

    reregistration_offer_button_text = keyboard_filler.reregistration_agree_button_text

    keyboard = [[InlineKeyboardButton(reregistration_offer_button_text, callback_data=REGISTRATION_YEAR)]]

    inline_markup = InlineKeyboardMarkup(keyboard)

    context.chat_data['message_id'] = bot.send_message(chat_id=chat_id, text = reregistration_message,
                                                       reply_markup=inline_markup).message_id

    print('routing to registration activity')

    return REGISTRATION_ACTIVITY_FLAG


def display_profile(update, context):
    print('---------------------------------------------------------------------')
    print('profile. display profile\n')

    chat_id = context.chat_data.get('chat_id')
    message_id = context.chat_data.get('message_id')

    bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id)

    user_id = context.chat_data.get('user_id')

    user = User.objects.get(telegram_id=user_id)

    profile = message_filler.profile
    fullname = message_filler.fullname
    spec = message_filler.spec
    group = message_filler.group
    subgroup = message_filler.subgroup

    message = f'''{profile}:

{fullname}: {user.full_name if user.full_name != None else '---'}
{spec}: {str(user.spec) if user.spec != None else '---'}
{group}: {str(user.group) if user.group != None else '---'}
{subgroup}: {user.subgroup if user.subgroup != 0 else '---'}
'''

    bot.send_message(chat_id=chat_id, text=message)

    return MAIN_ACTIVITY_FLAG