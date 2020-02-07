from django.core.management.base import BaseCommand
from telegram import Bot
from telegram.ext import Filters, CallbackContext, CommandHandler, MessageHandler, ConversationHandler, CallbackQueryHandler, Updater
import logging

from bot.models import Bot as DBBot

from .__utils import bot, MAIN_ACTIVITY_FLAG
from .__starting import start
from .__menu_management import manage_text_action

from .__utils import REGISTRATION_ACTIVITY_FLAG, REGISTRATION_END, REGISTRATION_GROUP, REGISTRATION_SPEC, REGISTRATION_FULLNAME
from .__utils import REGISTRATION_YEAR, REGISTRATION_SUBGROUP, REGISTRATION_TEXT_ACTIVITY_FLAG
from .__registration import choise_year, choise_spec, choise_group, choise_subgroup, complete_registration, ask_fullname

from .__utils import QUESTIONS_ACTIVITY_FLAG
from .__questions import save_question

from .__utils import SCHEDULE_ACTIVITY_FLAG, MY_SCHEDULE, OTHER_SCHEDULES, CHANGE_MY_GROUP
from .__utils import OTHER_SCHEDULE_GROUP, OTHER_SCHEDULE_SPEC
from .__utils import OTHER_SCHEDULE_SUBGROUP, OTHER_SCHEDULE_DISPLAY
from .__schedule import start_my_schedule_activity, start_other_schedules_activity, choise_spec as other_schedule_choise_spec
from .__schedule import choise_group as other_schedule_choise_group, choise_subgroup as other_schedule_choise_subgroup
from .__schedule import display_schedule as other_schedule_display_schedule

from .__utils import DISPLAY_NEWS, NEWS_ACTIVITY_FLAG
from .__news import start_news_activity, display_news

from .__utils import EXTRA_POINTS_ACTIVITY_FLAG, MY_EXTRA_POINTS, DOCS
from .__extra_points import display_extra_points, display_docs

from .__utils import MERCH_ACTIVITY_FLAG, DISPLAY_MERCH
from .__merch import display_merch

from .__utils import PROFILE_ACTIVITY_FLAG, PROFILE, REREGISTRATION
from .__profile import start_registration, display_profile

logging.basicConfig(format='%(asctime)s - %(name)s - %(message)s', level=logging.INFO)


class Command(BaseCommand):
    help = 'Telegram BOT'

    def handle(self, *args, **options):

        print('---------------------------------------------------------------------')
        print('Bot test:')

        bot_info = bot.get_me()

        db_bot = DBBot.objects.first()

        db_bot.telegram_id = bot_info.id
        db_bot.name = bot_info.first_name
        db_bot.nickname = bot_info.username

        db_bot.save()

        print(bot_info)
        print('---------------------------------------------------------------------')

        updater = Updater(bot=bot,
                          use_context=True)
        
        conversation_handler = ConversationHandler(
            entry_points=[CommandHandler('start', start)],
            states={
                MAIN_ACTIVITY_FLAG: [MessageHandler(Filters.text, manage_text_action)],

                SCHEDULE_ACTIVITY_FLAG: [CallbackQueryHandler(start_my_schedule_activity,
                                                pattern='^' + MY_SCHEDULE + '$'),
                                        CallbackQueryHandler(start_other_schedules_activity,
                                                pattern='^' + OTHER_SCHEDULES + '$'),
                                        CallbackQueryHandler(other_schedule_choise_spec,
                                                pattern='^' + OTHER_SCHEDULE_SPEC),
                                        CallbackQueryHandler(other_schedule_choise_group,
                                                pattern='^' + OTHER_SCHEDULE_GROUP),
                                        CallbackQueryHandler(other_schedule_choise_subgroup,
                                                pattern='^' + OTHER_SCHEDULE_SUBGROUP),
                                        CallbackQueryHandler(other_schedule_display_schedule,
                                                pattern='^' + OTHER_SCHEDULE_DISPLAY)],


                NEWS_ACTIVITY_FLAG: [CallbackQueryHandler(display_news,
                                                pattern='^' + DISPLAY_NEWS)],


                QUESTIONS_ACTIVITY_FLAG: [MessageHandler(Filters.text, save_question)],


                REGISTRATION_ACTIVITY_FLAG: [CallbackQueryHandler(choise_year,
                                                pattern='^' + REGISTRATION_YEAR + '$'), 
                                            CallbackQueryHandler(choise_spec,
                                                pattern='^' + REGISTRATION_SPEC),
                                            CallbackQueryHandler(choise_group,
                                                pattern='^' + REGISTRATION_GROUP),
                                            CallbackQueryHandler(choise_subgroup,
                                                pattern='^' + REGISTRATION_SUBGROUP),
                                            CallbackQueryHandler(ask_fullname,
                                                pattern='^' + REGISTRATION_FULLNAME)],
                REGISTRATION_TEXT_ACTIVITY_FLAG: [MessageHandler(Filters.text, complete_registration)],


                EXTRA_POINTS_ACTIVITY_FLAG: [CallbackQueryHandler(display_extra_points,
                                                pattern='^' + MY_EXTRA_POINTS + '$'),
                                            CallbackQueryHandler(display_docs,
                                                pattern='^' + DOCS + '$')],


                MERCH_ACTIVITY_FLAG: [CallbackQueryHandler(display_merch,
                                                pattern='^' + DISPLAY_MERCH)],


                PROFILE_ACTIVITY_FLAG: [CallbackQueryHandler(display_profile,
                                                pattern='^' + PROFILE + '$'),
                                        CallbackQueryHandler(start_registration,
                                                pattern='^' + REREGISTRATION + '$')]
            },
            fallbacks=[MessageHandler(Filters.text, manage_text_action), CommandHandler('start', start)]
        )

        updater.dispatcher.add_handler(conversation_handler)

        updater.start_polling()
        updater.idle()