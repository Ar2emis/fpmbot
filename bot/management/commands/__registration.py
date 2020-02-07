from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from .__utils import bot, MAIN_ACTIVITY_FLAG, REGISTRATION_END, REGISTRATION_GROUP, REGISTRATION_ACTIVITY_FLAG, REGISTRATION_TEXT_ACTIVITY_FLAG
from .__utils import REGISTRATION_SPEC, REGISTRATION_YEAR, REGISTRATION_SUBGROUP, REGISTRATION_FULLNAME, REGISTRATION_STUDENT_ID
from bot.models import Group, Spec, User
from .__fillers import RegistrationMessageFiller, RegistrationKeyboardFiller
from datetime import datetime
from .__starting import initialize_main_keyboard




message_filler = RegistrationMessageFiller()
keyboard_filler = RegistrationKeyboardFiller()



def choise_year(update, context):
    print('---------------------------------------------------------------------')
    print('registration. choise year\n')

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
                        callback_data=REGISTRATION_SPEC + ' ' + str(education_year - index))
        keyboard.append([course_button])

    inline_markup = InlineKeyboardMarkup(keyboard)

    context.chat_data['message_id'] = bot.send_message(chat_id=chat_id, text=message_filler.registration_year_question,
                                                       reply_markup=inline_markup).message_id

    print(f'Sent message: {context.chat_data.get("message_id")}')

    return REGISTRATION_ACTIVITY_FLAG


def choise_spec(update, context):
    print('---------------------------------------------------------------------')
    print('registration. choise spec\n')

    chat_id = context.chat_data.get('chat_id')
    last_message_id = context.chat_data.get('message_id')

    bot.edit_message_reply_markup(chat_id=chat_id, message_id=last_message_id, reply_markup=None)

    context.chat_data['year'] = int(update.callback_query.data.split(' ')[1])

    specs = Spec.objects.all()
    print(f'specs: {specs}')

    keyboard = []

    for spec in specs:
        keyboard.append([InlineKeyboardButton(str(spec), 
                         callback_data=REGISTRATION_GROUP + ' ' + str(spec.spec_id))])

    inline_markup = InlineKeyboardMarkup(keyboard)

    context.chat_data['message_id'] = bot.send_message(chat_id=chat_id, text=message_filler.registration_spec_question,
                                                       reply_markup=inline_markup).message_id

    print(f'sent message: {context.chat_data.get("message_id")}')

    return REGISTRATION_ACTIVITY_FLAG


def choise_group(update, context):
    print('---------------------------------------------------------------------')
    print('registration. choise group\n')

    chat_id = context.chat_data.get('chat_id')
    last_message_id = context.chat_data.get('message_id')

    bot.edit_message_reply_markup(chat_id=chat_id, message_id=last_message_id, reply_markup=None)

    year = context.chat_data.get('year')
    spec_id = int(update.callback_query.data.split(' ')[1])
    context.chat_data['spec_id'] = spec_id

    groups = Group.objects.all().filter(year=year, spec__spec_id=spec_id)

    if len(groups) == 0:
        print('---No groups for this year---')

        reply_markup = initialize_main_keyboard()

        group_not_found_message = message_filler.registration_group_not_found_message

        bot.send_message(chat_id=chat_id, text=group_not_found_message, reply_markup=reply_markup)

        return MAIN_ACTIVITY_FLAG

    print(groups)

    keyboard = []

    for group in groups:
        keyboard.append([InlineKeyboardButton(str(group), 
                         callback_data=REGISTRATION_SUBGROUP + ' ' + str(group.pk))])

    inline_markup = InlineKeyboardMarkup(keyboard)
    print(inline_markup)

    context.chat_data['message_id'] = bot.send_message(chat_id=chat_id, text=message_filler.registration_group_question,
                                                       reply_markup=inline_markup).message_id

    print(f'sent message: {context.chat_data.get("message_id")}')

    return REGISTRATION_ACTIVITY_FLAG


def choise_subgroup(update, context):
    print('---------------------------------------------------------------------')
    print('registration. choise subgroup\n')

    chat_id = context.chat_data.get('chat_id')
    last_message_id = context.chat_data.get('message_id')

    bot.edit_message_reply_markup(chat_id=chat_id, message_id=last_message_id, reply_markup=None)

    group_pk = int(update.callback_query.data.split(' ')[1])
    context.chat_data['group_pk'] = group_pk

    group = Group.objects.get(pk=group_pk)
    print(f'subgroup: {group.subgroup_amount}')

    if group.subgroup_amount == 0:
        context.chat_data['is_subgroups_zero'] = True
        return ask_fullname(update, context)

    context.chat_data['is_subgroups_zero'] = False
    keyboard = []

    for subgroup_number in range(1, group.subgroup_amount + 1):
        print(subgroup_number)
        keyboard.append([InlineKeyboardButton(str(subgroup_number),
                         callback_data=REGISTRATION_FULLNAME + ' ' + str(subgroup_number))])

    inline_markup = InlineKeyboardMarkup(keyboard)
    print(inline_markup)

    context.chat_data['message_id'] = bot.send_message(chat_id=chat_id, text=message_filler.registration_subgroup_question,
                                                       reply_markup=inline_markup).message_id

    print(f'sent message: {context.chat_data.get("message_id")}')

    return REGISTRATION_ACTIVITY_FLAG


def ask_fullname(update, context):
    print('---------------------------------------------------------------------')
    print('registration. ask full name\n')

    chat_id = context.chat_data.get('chat_id')
    is_subgroups_zero = context.chat_data.get('is_subgroups_zero')
    if is_subgroups_zero:
        context.chat_data['subgroup'] = 0
    else:
        last_message_id = context.chat_data.get('message_id')

        bot.edit_message_reply_markup(chat_id=chat_id, message_id=last_message_id, reply_markup=None)

        context.chat_data['subgroup'] = int(update.callback_query.data.split(' ')[1])

    bot.send_message(chat_id=chat_id, text=message_filler.registration_fullname_question)

    return REGISTRATION_TEXT_ACTIVITY_FLAG


def complete_registration(update, context):
    print('---------------------------------------------------------------------')
    print('registration. completing\n')

    chat_id = context.chat_data.get('chat_id')

    fullname = update.message.text
    print(f'fullname: {fullname}')

    telegram_id = context.chat_data.get('user_id')
    user = User.objects.get(telegram_id=telegram_id)
    print(f'user: {user}')

    spec_id = context.chat_data.get('spec_id')
    spec = Spec.objects.get(spec_id=spec_id)
    print(f'spec: {spec}')

    group_pk = context.chat_data.get('group_pk')
    group = Group.objects.get(pk=group_pk)
    print(f'group: {group}')

    subgroup = context.chat_data.get('subgroup')
    print(f'subgroup: {subgroup}')

    user.full_name = fullname
    user.spec = spec
    user.group = group
    user.subgroup = subgroup
    user.save()

    reply_markup = initialize_main_keyboard()

    context.chat_data['message_id'] = bot.send_message(chat_id=chat_id, text=message_filler.registration_completing_text,
                                                       reply_markup=reply_markup).message_id

    print(f'sent message: {context.chat_data.get("message_id")}')

    return MAIN_ACTIVITY_FLAG