from .__utils import MAIN_ACTIVITY_FLAG
from bot.models import Text
from .__contacts import start_contacts_activity
from .__questions import start_questions_activity
from .__schedule import start_schedule_activity
from .__news import start_news_activity
from .__extra_points import start_extra_points_activity
from .__fillers import ManagementFiller
from .__merch import start_merch_activity
from .__profile import start_profile_activity




def manage_text_action(update, context):

    text = update.message.text

    manager = ManagementFiller()
    
    schedule = manager.schedule
    questions = manager.questions
    news = manager.news
    contacts = manager.contacts
    merch = manager.merch
    extra_points = manager.extra_points
    profile = manager.profile

    if text == schedule:
        print(schedule)
        return start_schedule_activity(update, context)

    elif text == questions:
        print(questions)
        return start_questions_activity(update, context)

    elif text == news:
        print(news)
        return start_news_activity(update, context)

    elif text == contacts:
        print(contacts)
        return start_contacts_activity(update,context)

    elif text == merch:
        print(merch)
        return start_merch_activity(update, context)

    elif text == extra_points:
        print(extra_points)
        return start_extra_points_activity(update, context)

    elif text == profile:
        print(profile)
        return start_profile_activity(update, context)

    return MAIN_ACTIVITY_FLAG