from .__utils import QUESTIONS_ACTIVITY_FLAG, bot, MAIN_ACTIVITY_FLAG
from .__fillers import QuestionsMessageFiller, TextFiltrator
from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton
from bot.models import Question, User




message_filler = QuestionsMessageFiller()




def start_questions_activity(update, context):
    print('---------------------------------------------------------------------')
    print('questions. offer question\n')

    chat_id = context.chat_data.get('chat_id')

    offer_question_message = message_filler.questions_offer_message

    bot.send_message(chat_id=chat_id, text=offer_question_message)

    return QUESTIONS_ACTIVITY_FLAG


def save_question(update, context):
    print('---------------------------------------------------------------------')
    print('questions. save question\n')

    question_text = update.message.text
    print(f'question:\n{question_text}')

    if TextFiltrator().check_for_main_menu_keyboard(question_text):
        return MAIN_ACTIVITY_FLAG

    user_first_name = update.message.from_user.first_name
    user_last_name = update.message.from_user.last_name

    telegram_full_name = f'{user_first_name} {user_last_name}' if user_last_name != None else user_first_name

    telegram_username = update.message.from_user.username
    
    question = Question()
    
    user_id = context.chat_data['user_id']

    user = User.objects.filter(telegram_id=user_id).first()
    user.telegram_name = telegram_full_name
    user.telegram_username = telegram_username
    user.save()

    question.sender = user
    question.text = question_text
    question.save()

    chat_id = context.chat_data.get('chat_id')
    thanks_for_question_message = message_filler.thanks_for_question_message

    bot.send_message(chat_id=chat_id, text=thanks_for_question_message)

    return MAIN_ACTIVITY_FLAG





