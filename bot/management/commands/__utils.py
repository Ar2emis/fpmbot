from telegram import Bot
from telegram.utils.request import Request
from bot import models




bot = Bot(request=Request(con_pool_size=8,
                          connect_timeout=0.5,
                          read_timeout=1.0),
                  token=models.Bot.objects.first().token)




MAIN_ACTIVITY_FLAG = 1


CONTACTS_ACTIVITY_FLAG = 50


SCHEDULE_ACTIVITY_FLAG = 10
MY_SCHEDULE = 'my_schedule'
OTHER_SCHEDULE_SPEC = 'other_schedules.spec'
OTHER_SCHEDULE_GROUP = 'other_schedules.group'
OTHER_SCHEDULE_SUBGROUP = 'other_schedules.subgroup'
OTHER_SCHEDULE_DISPLAY = 'other_schedules.display'
OTHER_SCHEDULES = 'other_schedules'
CHANGE_MY_GROUP = 'change_my_group'


NEWS_ACTIVITY_FLAG = 40
DISPLAY_NEWS = 'news.display'


QUESTIONS_ACTIVITY_FLAG = 30


REGISTRATION_ACTIVITY_FLAG = 20
REGISTRATION_YEAR = 'registration.year'
REGISTRATION_SPEC = 'registration.spec'
REGISTRATION_GROUP = 'registration.group'
REGISTRATION_SUBGROUP = 'registration.subgroup'
REGISTRATION_TEXT_ACTIVITY_FLAG = 21
REGISTRATION_FULLNAME = 'registration.full_name'
REGISTRATION_STUDENT_ID = 'registration.student_id'
REGISTRATION_END = 'registration.end'


EXTRA_POINTS_ACTIVITY_FLAG = 60
MY_EXTRA_POINTS = 'my_extra_points'
DOCS = 'docs'


MERCH_ACTIVITY_FLAG = 70
DISPLAY_MERCH = 'display_merch'

PROFILE_ACTIVITY_FLAG = 80
PROFILE = 'profile'
REREGISTRATION = 'reregistration'