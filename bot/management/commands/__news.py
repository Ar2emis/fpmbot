from .__utils import bot, MAIN_ACTIVITY_FLAG, NEWS_ACTIVITY_FLAG, DISPLAY_NEWS
from .__fillers import NewsMessageFiller, NewsKeyboardFiller
from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from bot.models import NewsCategory, News
from datetime import datetime




message_filler = NewsMessageFiller()
keyboard_filler = NewsKeyboardFiller()




def start_news_activity(update, context):
    print('---------------------------------------------------------------------')
    print('news. start news activity\n')

    chat_id = context.chat_data.get('chat_id')

    news_start_message = message_filler.news_start_message

    all_news_button_text = keyboard_filler.all_news_button_text

    ALL_NEWS_FLAG = 0

    keyboard = [[InlineKeyboardButton(all_news_button_text,
                                      callback_data=DISPLAY_NEWS + ' ' + str(ALL_NEWS_FLAG))]]

    categories = NewsCategory.objects.all()

    for category in categories:
        keyboard.append([InlineKeyboardButton(category.name,
                                              callback_data=DISPLAY_NEWS + ' ' + str(category.pk))])

    inline_markup = InlineKeyboardMarkup(keyboard)

    context.chat_data['message_id'] = bot.send_message(chat_id=chat_id, text=news_start_message,
                                                       reply_markup=inline_markup).message_id

    return NEWS_ACTIVITY_FLAG


def display_news(update, context):
    print('---------------------------------------------------------------------')
    print('news. display news\n')

    chat_id = context.chat_data.get('chat_id')
    message_id = context.chat_data.get('message_id')

    bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id)

    category_pk = int(update.callback_query.data.split(' ')[1])

    news = None
    if category_pk == 0:
        news = News.objects.all().filter(limit_date__gt=datetime.today())
    else:
        news = News.objects.all().filter(category__pk=category_pk, limit_date__gt=datetime.today())

    print(news)

    if len(news) == 0:
        bot.send_message(chat_id=chat_id, text=message_filler.no_news_found_message)
    else:
        bot.send_message(chat_id=chat_id, text=message_filler.news_found_message)

        for item in news:
            images = []

            for image in item.images.all():
                images.append(InputMediaPhoto(open(image.image_file.path, 'rb')))

            images[0].caption = item.text

            bot.send_media_group(chat_id=chat_id, media=images)

    return MAIN_ACTIVITY_FLAG