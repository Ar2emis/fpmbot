from .__utils import bot, MAIN_ACTIVITY_FLAG, EXTRA_POINTS_ACTIVITY_FLAG, MY_EXTRA_POINTS, DOCS
from .__fillers import ExtraPointsMessageFiller, ExtraPointsKeyboardFiller
from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton
from bot.models import Event, User, Doc
from datetime import datetime, date




message_filler = ExtraPointsMessageFiller()
keyboard_filler = ExtraPointsKeyboardFiller()




def start_extra_points_activity(update, context):
    print('---------------------------------------------------------------------')
    print('extra points. start extra points activity\n')

    chat_id = context.chat_data.get('chat_id')

    message = message_filler.start_message

    keyboard = keyboard_filler.extra_points_keyboard

    inline_keyboard = [[InlineKeyboardButton(keyboard[0][0], callback_data=MY_EXTRA_POINTS)],
                       [InlineKeyboardButton(keyboard[1][0], callback_data=DOCS)]]

    inline_markup = InlineKeyboardMarkup(inline_keyboard)

    context.chat_data['message_id'] = bot.send_message(chat_id=chat_id, text=message,
                                      reply_markup=inline_markup).message_id

    return EXTRA_POINTS_ACTIVITY_FLAG


def display_extra_points(update, context):
    print('---------------------------------------------------------------------')
    print('extra points. display extra points\n')

    chat_id = context.chat_data.get('chat_id')
    last_message_id = context.chat_data.get('message_id')

    bot.edit_message_reply_markup(chat_id=chat_id, message_id=last_message_id)

    user_id = context.chat_data.get('user_id')
    user = User.objects.get(telegram_id=user_id)

    today = datetime.today()

    separate_date = None

    MIDDLE_MONTH = 7

    if today.month < MIDDLE_MONTH:
        separate_date = date(today.year, 1, 1)
    else:
        separate_date = date(today.year, MIDDLE_MONTH, 1)

    events = Event.objects.filter(participants=user, added_date__gte=separate_date)
    print(f'events: {events}')

    if len(events) == 0:
        bot.send_message(chat_id=chat_id, text=message_filler.no_extra_points_message)
        return MAIN_ACTIVITY_FLAG

    bot.send_message(chat_id=chat_id, text=message_filler.before_extra_points_message)

    event_name = message_filler.event_name
    paragraph = message_filler.paragraph
    max_points = message_filler.max_points
    actual_points = message_filler.actual_points
    summary = message_filler.summary

    message = ''
    sum = 0
    for event in events:
        message += f'''{event_name}: {event.name}
{paragraph}: {event.paragraph}
{max_points}: {event.max_points}
{actual_points}: {event.actual_points}\n\n'''

        sum += event.actual_points

    message += f'{summary}: {sum}'
    print(message)

    bot.send_message(chat_id=chat_id, text=message)

    return MAIN_ACTIVITY_FLAG


def display_docs(update, context):
    print('---------------------------------------------------------------------')
    print('extra points. display docs\n')
    
    chat_id = context.chat_data.get('chat_id')
    last_message_id = context.chat_data.get('message_id')

    bot.edit_message_reply_markup(chat_id=chat_id, message_id=last_message_id)

    GROUP = 'Extra points'

    docs = Doc.objects.filter(group=GROUP)

    for doc in docs:
        bot.send_document(chat_id=chat_id, document=open(doc.file.path, 'rb'), filename=doc.name)
        
    return MAIN_ACTIVITY_FLAG