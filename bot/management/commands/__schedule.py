from bot.models import User, Schedule, Spec, Group
from .__utils import bot, MAIN_ACTIVITY_FLAG, SCHEDULE_ACTIVITY_FLAG, REGISTRATION_YEAR, REGISTRATION_ACTIVITY_FLAG
from .__utils import MY_SCHEDULE, OTHER_SCHEDULES, CHANGE_MY_GROUP
from .__utils import OTHER_SCHEDULE_SPEC, OTHER_SCHEDULE_GROUP, OTHER_SCHEDULE_SUBGROUP, OTHER_SCHEDULE_DISPLAY
from .__fillers import ScheduleMessageFiller, ScheduleKeyboardFiller
from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime




message_filler = ScheduleMessageFiller()
keyboard_filler = ScheduleKeyboardFiller()




def start_schedule_activity(update, context):
    print('---------------------------------------------------------------------')
    print('schedule. start shcedule activity\n')

    chat_id = context.chat_data.get('chat_id')

    start_schedule_activity_message = message_filler.start_schedule_activity_message

    my_schedule_button = InlineKeyboardButton(keyboard_filler.my_schedule_button_text, 
                                              callback_data=MY_SCHEDULE)

    other_schedules_button = InlineKeyboardButton(keyboard_filler.other_schedules_button_text, 
                                              callback_data=OTHER_SCHEDULES)

    keyboard = [[my_schedule_button],
                [other_schedules_button]]

    inline_markup = InlineKeyboardMarkup(keyboard)

    context.chat_data['message_id'] = bot.send_message(chat_id=chat_id, text=start_schedule_activity_message, 
                                                       reply_markup=inline_markup).message_id

    return SCHEDULE_ACTIVITY_FLAG




def start_my_schedule_activity(update, context):
    print('---------------------------------------------------------------------')
    print('schedule. start my schedule activity\n')

    chat_id = context.chat_data.get('chat_id')
    message_id = context.chat_data.get('message_id')

    bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id)

    user_id = context.chat_data.get('user_id')

    user = User.objects.get(telegram_id=user_id)

    if user.group is None:
        print('---unregistered user---')

        unregistered_user_message = message_filler.unregistered_user_message

        bot.send_message(chat_id=chat_id, text=unregistered_user_message)

        return MAIN_ACTIVITY_FLAG

    schedule = Schedule.objects.filter(group=user.group, subgroup=user.subgroup).first()

    if schedule == None:
        print('---no schedule by this parameters---')

        no_schedule_message = message_filler.schedule_not_found_message

        bot.send_message(chat_id=chat_id, text=no_schedule_message)
    else:
        bot_before_schedule_message = message_filler.before_display_schedule_message

        bot.send_message(chat_id=chat_id, text=bot_before_schedule_message)

        schedule_message = schedule.schedule

        bot.send_message(chat_id=chat_id, text=schedule_message)

    return MAIN_ACTIVITY_FLAG




def start_other_schedules_activity(update, context):
    print('---------------------------------------------------------------------')
    print('schedule. start other schedules activity. choise course\n')

    chat_id = context.chat_data.get('chat_id')
    last_message_id = context.chat_data.get('message_id')

    bot.edit_message_reply_markup(chat_id=chat_id, message_id=last_message_id, reply_markup=None)

    years = keyboard_filler.courses_buttons_texts
    current_date = datetime.today()

    SEPTEMBER = 9
    education_year = 0

    if current_date.month < SEPTEMBER:
        education_year = current_date.year - 1
    else:
        education_year = current_date.year

    keyboard = []

    COURSES_AMOUNT = 6

    for index in range(0, COURSES_AMOUNT):
        course_button = InlineKeyboardButton(years[index],
                        callback_data=OTHER_SCHEDULE_SPEC + ' ' + str(education_year - index))
        keyboard.append([course_button])

    inline_markup = InlineKeyboardMarkup(keyboard)

    context.chat_data['message_id'] = bot.send_message(chat_id=chat_id, text=message_filler.choise_course_message,
                                                       reply_markup=inline_markup).message_id

    print(f'Sent message: {context.chat_data.get("message_id")}')

    return SCHEDULE_ACTIVITY_FLAG


def choise_spec(update, context):
    print('---------------------------------------------------------------------')
    print('schedule. other schedules. choise spec\n')

    chat_id = context.chat_data.get('chat_id')
    last_message_id = context.chat_data.get('message_id')

    bot.edit_message_reply_markup(chat_id=chat_id, message_id=last_message_id, reply_markup=None)

    context.chat_data['year'] = int(update.callback_query.data.split(' ')[1])

    specs = Spec.objects.all()
    print(f'specs: {specs}')

    keyboard = []

    for spec in specs:
        keyboard.append([InlineKeyboardButton(str(spec), 
                         callback_data=str(OTHER_SCHEDULE_GROUP) + ' ' + str(spec.spec_id))])

    inline_markup = InlineKeyboardMarkup(keyboard)

    context.chat_data['message_id'] = bot.send_message(chat_id=chat_id, text=message_filler.choise_spec_message,
                                                       reply_markup=inline_markup).message_id

    print(f'sent message: {context.chat_data.get("message_id")}')

    return SCHEDULE_ACTIVITY_FLAG


def choise_group(update, context):
    print('---------------------------------------------------------------------')
    print('schedule. other schedules. choise group\n')

    chat_id = context.chat_data.get('chat_id')
    last_message_id = context.chat_data.get('message_id')

    bot.edit_message_reply_markup(chat_id=chat_id, message_id=last_message_id, reply_markup=None)

    year = context.chat_data.get('year')
    spec_id = int(update.callback_query.data.split(' ')[1])
    context.chat_data['spec_id'] = spec_id

    groups = Group.objects.all().filter(year=year, spec__spec_id=spec_id)

    if len(groups) == 0:
        print('---No groups for this year---')

        group_not_found_message = message_filler.group_not_found_message

        bot.send_message(chat_id=chat_id, text=group_not_found_message)

        return MAIN_ACTIVITY_FLAG

    print(groups)

    keyboard = []

    for group in groups:
        keyboard.append([InlineKeyboardButton(str(group), 
                         callback_data=str(OTHER_SCHEDULE_SUBGROUP) + ' ' + str(group.pk))])

    inline_markup = InlineKeyboardMarkup(keyboard)
    print(inline_markup)

    context.chat_data['message_id'] = bot.send_message(chat_id=chat_id, text=message_filler.choise_group_message,
                                                       reply_markup=inline_markup).message_id

    print(f'sent message: {context.chat_data.get("message_id")}')

    return SCHEDULE_ACTIVITY_FLAG


def choise_subgroup(update, context):
    print('---------------------------------------------------------------------')
    print('schedule. other schedules. choise subgroup\n')

    chat_id = context.chat_data.get('chat_id')
    last_message_id = context.chat_data.get('message_id')

    bot.edit_message_reply_markup(chat_id=chat_id, message_id=last_message_id, reply_markup=None)

    group_pk = int(update.callback_query.data.split(' ')[1])
    context.chat_data['group_pk'] = group_pk

    group = Group.objects.get(pk=group_pk)
    print(f'subgroup: {group.subgroup_amount}')

    if group.subgroup_amount == 0:
        context.chat_data['is_subgroups_zero'] = True
        return display_schedule(update, context)

    context.chat_data['is_subgroups_zero'] = False
    keyboard = []

    for subgroup_number in range(1, group.subgroup_amount + 1):
        print(subgroup_number)
        keyboard.append([InlineKeyboardButton(str(subgroup_number),
                        callback_data=str(OTHER_SCHEDULE_DISPLAY) + ' ' + str(subgroup_number))])

    inline_markup = InlineKeyboardMarkup(keyboard)
    print(inline_markup)

    context.chat_data['message_id'] = bot.send_message(chat_id=chat_id, text=message_filler.choise_subgroup_message,
                                                    reply_markup=inline_markup).message_id

    print(f'sent message: {context.chat_data.get("message_id")}')

    return SCHEDULE_ACTIVITY_FLAG


def display_schedule(update, context):
    print('---------------------------------------------------------------------')
    print('schedule. other schedules. display schedule\n')

    chat_id = context.chat_data.get('chat_id')

    group_pk = context.chat_data.get('group_pk')

    group = Group.objects.get(pk=group_pk)
    subgroup = 0

    is_subgroups_zero = context.chat_data.get('is_subgroups_zero')
    if not is_subgroups_zero:
        last_message_id = context.chat_data.get('message_id')
        bot.edit_message_reply_markup(chat_id=chat_id, message_id=last_message_id, reply_markup=None)

        subgroup = int(update.callback_query.data.split(' ')[1])

    schedule = Schedule.objects.filter(group=group, subgroup=subgroup).first()

    if schedule == None:
        bot.send_message(chat_id=chat_id, text=message_filler.schedule_not_found_message)
    else:
        bot.send_message(chat_id=chat_id, text=message_filler.before_display_schedule_message)
        bot.send_message(chat_id=chat_id, text=schedule.schedule)

    return MAIN_ACTIVITY_FLAG