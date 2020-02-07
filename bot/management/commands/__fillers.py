from bot.models import Text





class TextFiltrator:

    def check_for_main_menu_keyboard(self, text):
        SCHEDULE_NAME = 'Main menu schedule'
        QUESTIONS_NAME = 'Main menu questions'
        NEWS_NAME = 'Main menu news'
        CONTACTS_NAME = 'Main menu contacts'
        MERCH_NAME = 'Main menu merch'
        EXTRA_POINTS_NAME = 'Main menu extra points'
        PROFILE_NAME = 'Main menu profile'

        schedule = Text.objects.get(name=SCHEDULE_NAME).text
        questions = Text.objects.get(name=QUESTIONS_NAME).text
        news = Text.objects.get(name=NEWS_NAME).text
        contacts = Text.objects.get(name=CONTACTS_NAME).text
        merch = Text.objects.get(name=MERCH_NAME).text
        extra_points = Text.objects.get(name=EXTRA_POINTS_NAME).text
        profile = Text.objects.get(name=PROFILE_NAME).text

        main_menu_keyboard = []
        main_menu_keyboard.append(schedule)
        main_menu_keyboard.append(news)
        main_menu_keyboard.append(questions)
        main_menu_keyboard.append(contacts)
        main_menu_keyboard.append(merch)
        main_menu_keyboard.append(extra_points)
        main_menu_keyboard.append(profile)

        for button in main_menu_keyboard:
            if button == text:
                return True
        
        return False


class StartKeyboardFiller:

    main_menu_keyboard = []
    registration_offer_keyboard = []

    def __init__(self):
        SCHEDULE_NAME = 'Main menu schedule'
        QUESTIONS_NAME = 'Main menu questions'
        NEWS_NAME = 'Main menu news'
        CONTACTS_NAME = 'Main menu contacts'
        REGISTRATION_OFFER_NAME = 'Registration beginning'
        MERCH_NAME = 'Main menu merch'
        EXTRA_POINTS_NAME = 'Main menu extra points'
        PROFILE_NAME = 'Main menu profile'
        
        schedule = Text.objects.get(name=SCHEDULE_NAME).text
        questions = Text.objects.get(name=QUESTIONS_NAME).text
        news = Text.objects.get(name=NEWS_NAME).text
        contacts = Text.objects.get(name=CONTACTS_NAME).text
        merch = Text.objects.get(name=MERCH_NAME).text
        extra_points = Text.objects.get(name=EXTRA_POINTS_NAME).text
        profile = Text.objects.get(name=PROFILE_NAME).text

        self.main_menu_keyboard.append([schedule, news])
        self.main_menu_keyboard.append([questions, contacts])
        self.main_menu_keyboard.append([merch, extra_points])
        self.main_menu_keyboard.append([profile])

        registration_offer_button = Text.objects.get(name=REGISTRATION_OFFER_NAME).text
        self.registration_offer_keyboard.append([registration_offer_button])


class StartMessageFiller:

    def __init__(self):
        START_HELLO_NAME = 'Hello message'
        NEW_USER_START_ENDING_NAME = 'New user start'
        OLD_USER_START_ENDING_NAME = 'Old user start'

        self.start_hello_message = Text.objects.get(name=START_HELLO_NAME).text
        self.new_user_start_ending_message = Text.objects.get(name=NEW_USER_START_ENDING_NAME).text
        self.old_user_start_ending_message = Text.objects.get(name=OLD_USER_START_ENDING_NAME).text

        


class RegistrationMessageFiller:

    def __init__(self):
        REGISTRATION_YEAR_ASKING_NAME = 'Registration year asking'
        REGISTRATION_SPEC_ASKING_NAME = 'Registration spec asking'
        REGISTRATION_GROUP_ASKING_NAME = 'Registration spec asking'
        REGISTRATION_SUBGROUP_ASKING_NAME = 'Registration subgroup asking'
        REGISTRATION_COMPLETING_NAME = 'Registration completing'
        REGISTRATION_GROUP_NOT_FOUND_NAME = 'Registration group not found message'
        REGISTRATION_FULLNAME_ASKING_NAME = 'Registration fullname asking'

        self.registration_year_question = Text.objects.get(name=REGISTRATION_YEAR_ASKING_NAME).text
        self.registration_spec_question = Text.objects.get(name=REGISTRATION_SPEC_ASKING_NAME).text
        self.registration_group_question = Text.objects.get(name=REGISTRATION_GROUP_ASKING_NAME).text
        self.registration_subgroup_question = Text.objects.get(name=REGISTRATION_SUBGROUP_ASKING_NAME).text
        self.registration_completing_text = Text.objects.get(name=REGISTRATION_COMPLETING_NAME).text
        self.registration_group_not_found_message = Text.objects.get(name=REGISTRATION_GROUP_NOT_FOUND_NAME).text
        self.registration_fullname_question = Text.objects.get(name=REGISTRATION_FULLNAME_ASKING_NAME).text


class RegistrationKeyboardFiller:

    main_menu_keyboard = []

    def __init__(self):
        REGISTRATION_FIRST_COURSE_NAME = 'Registration 1 course button'
        REGISTRATION_SECOND_COURSE_NAME = 'Registration 2 course button'
        REGISTRATION_THIRD_COURSE_NAME = 'Registration 3 course button'
        REGISTRATION_FOURTH_COURSE_NAME = 'Registration 4 course button'
        REGISTRATION_FIVTH_COURSE_NAME = 'Registration 5 course button'
        REGISTRATION_SIXTH_COURSE_NAME = 'Registration 6 course button'
        SCHEDULE_NAME = 'Main menu schedule'
        QUESTIONS_NAME = 'Main menu questions'
        NEWS_NAME = 'Main menu news'
        CONTACTS_NAME = 'Main menu contacts'
        MERCH_NAME = 'Main menu merch'
        EXTRA_POINTS_NAME = 'Main menu extra points'

        schedule = Text.objects.get(name=SCHEDULE_NAME).text
        questions = Text.objects.get(name=QUESTIONS_NAME).text
        news = Text.objects.get(name=NEWS_NAME).text
        contacts = Text.objects.get(name=CONTACTS_NAME).text
        merch = Text.objects.get(name=MERCH_NAME).text
        extra_points = Text.objects.get(name=EXTRA_POINTS_NAME).text

        self.main_menu_keyboard.append([schedule, news])
        self.main_menu_keyboard.append([questions, contacts])
        self.main_menu_keyboard.append([merch, extra_points])

        first_course_button_text = Text.objects.get(name=REGISTRATION_FIRST_COURSE_NAME).text
        second_course_button_text = Text.objects.get(name=REGISTRATION_SECOND_COURSE_NAME).text
        third_course_button_text = Text.objects.get(name=REGISTRATION_THIRD_COURSE_NAME).text
        fourth_course_button_text = Text.objects.get(name=REGISTRATION_FOURTH_COURSE_NAME).text
        fivth_course_button_text = Text.objects.get(name=REGISTRATION_FIVTH_COURSE_NAME).text
        sixth_course_button_text = Text.objects.get(name=REGISTRATION_SIXTH_COURSE_NAME).text

        courses = [first_course_button_text,
                   second_course_button_text,
                   third_course_button_text,
                   fourth_course_button_text,
                   fivth_course_button_text,
                   sixth_course_button_text]

        self.courses_buttons_texts = courses



class ContactsMessageFiller:

    def __init__(self):
        CONTACTS_NAME = 'Contacts message'

        self.contacts_message = Text.objects.get(name=CONTACTS_NAME).text




class QuestionsMessageFiller:

    def __init__(self):
        QUESTIONS_OFFER_NAME = 'Questions offer message'
        THANKS_FOR_QUESTION_NAME = 'Thanks for question message'

        self.questions_offer_message = Text.objects.get(name=QUESTIONS_OFFER_NAME).text
        self.thanks_for_question_message = Text.objects.get(name=THANKS_FOR_QUESTION_NAME).text




class ScheduleMessageFiller:
    
    def __init__(self):
        START_SCHEDULE_NAME = 'Start Schedule message'
        UNREGISTERED_USER_NAME = 'Unregistered user message'
        SCHEDULE_NOT_FOUND_NAME = 'Schedule not found message'
        BEFORE_DISPLAY_SCHEDULE_NAME = 'Schedule before display schedule message'
        CHOISE_COURSE_NAME = 'Schedule choise course message'
        CHOISE_SPEC_NAME = 'Schedule choise spec message'
        CHOISE_GROUP_NAME = 'Schedule choise group message'
        CHOISE_SUBGROUP_NAME = 'Schedule choise subgroup message'
        GROUP_NOT_FOUND_NAME = 'Schedule group not found message'

        self.start_schedule_activity_message = Text.objects.get(name=START_SCHEDULE_NAME).text
        self.unregistered_user_message = Text.objects.get(name=UNREGISTERED_USER_NAME).text
        self.schedule_not_found_message = Text.objects.get(name=SCHEDULE_NOT_FOUND_NAME).text
        self.before_display_schedule_message = Text.objects.get(name=BEFORE_DISPLAY_SCHEDULE_NAME).text
        self.choise_course_message = Text.objects.get(name=CHOISE_COURSE_NAME).text
        self.choise_spec_message = Text.objects.get(name=CHOISE_SPEC_NAME).text
        self.choise_group_message = Text.objects.get(name=CHOISE_GROUP_NAME).text
        self.choise_subgroup_message = Text.objects.get(name=CHOISE_SUBGROUP_NAME).text
        self.group_not_found_message = Text.objects.get(name=GROUP_NOT_FOUND_NAME).text


class ScheduleKeyboardFiller:
    
    def __init__(self):
        MY_SCHEDULE_NAME = 'My Schedule button'
        OTHER_SCHEDULES_NAME = 'Other schedules button'

        self.my_schedule_button_text = Text.objects.get(name=MY_SCHEDULE_NAME).text
        self.other_schedules_button_text = Text.objects.get(name=OTHER_SCHEDULES_NAME).text

        REGISTRATION_FIRST_COURSE_NAME = 'Registration 1 course button'
        REGISTRATION_SECOND_COURSE_NAME = 'Registration 2 course button'
        REGISTRATION_THIRD_COURSE_NAME = 'Registration 3 course button'
        REGISTRATION_FOURTH_COURSE_NAME = 'Registration 4 course button'
        REGISTRATION_FIVTH_COURSE_NAME = 'Registration 5 course button'
        REGISTRATION_SIXTH_COURSE_NAME = 'Registration 6 course button'

        first_course_button_text = Text.objects.get(name=REGISTRATION_FIRST_COURSE_NAME).text
        second_course_button_text = Text.objects.get(name=REGISTRATION_SECOND_COURSE_NAME).text
        third_course_button_text = Text.objects.get(name=REGISTRATION_THIRD_COURSE_NAME).text
        fourth_course_button_text = Text.objects.get(name=REGISTRATION_FOURTH_COURSE_NAME).text
        fivth_course_button_text = Text.objects.get(name=REGISTRATION_FIVTH_COURSE_NAME).text
        sixth_course_button_text = Text.objects.get(name=REGISTRATION_SIXTH_COURSE_NAME).text

        courses = [first_course_button_text,
                   second_course_button_text,
                   third_course_button_text,
                   fourth_course_button_text,
                   fivth_course_button_text,
                   sixth_course_button_text]

        self.courses_buttons_texts = courses




class NewsMessageFiller:
    
    def __init__(self):
        NEWS_START_NAME = 'News start message'
        NO_NEWS_FOUND_NAME = 'No news found message'
        NEWS_FOUND_NAME = 'News found message'

        self.news_start_message = Text.objects.get(name=NEWS_START_NAME).text
        self.no_news_found_message = Text.objects.get(name=NO_NEWS_FOUND_NAME).text
        self.news_found_message = Text.objects.get(name=NEWS_FOUND_NAME).text


class NewsKeyboardFiller:

    def __init__(self):
        ALL_NEWS_NAME = 'All news button'

        self.all_news_button_text = Text.objects.get(name=ALL_NEWS_NAME).text




class ExtraPointsMessageFiller:

    def __init__(self):
        START_NAME = 'Extra points start message'
        NO_EXTRA_POINTS_NAME = 'Extra points no extra points message'
        BEFORE_POINTS_NAME = 'Extra points before display points message'
        EVENT_NAME = 'Extra points event'
        PARAGRAPH_NAME = 'Extra points paragraph'
        MAX_POINTS_NAME = 'Extra points max points'
        ACTUAL_POINTS_NAME = 'Extra points actual points'
        SUMMARY_NAME = 'Extra points summary'

        self.start_message = Text.objects.get(name=START_NAME).text
        self.no_extra_points_message = Text.objects.get(name=NO_EXTRA_POINTS_NAME).text
        self.before_extra_points_message = Text.objects.get(name=BEFORE_POINTS_NAME).text
        self.event_name = Text.objects.get(name=EVENT_NAME).text
        self.paragraph = Text.objects.get(name=PARAGRAPH_NAME).text
        self.max_points = Text.objects.get(name=MAX_POINTS_NAME).text
        self.actual_points = Text.objects.get(name=ACTUAL_POINTS_NAME).text
        self.summary = Text.objects.get(name=SUMMARY_NAME).text


class ExtraPointsKeyboardFiller:

    def __init__(self):
        MY_POINTS_NAME = 'Extra points my points button'
        DOCS_NAME = 'Extra points docs button'

        my_points_text = Text.objects.get(name=MY_POINTS_NAME).text
        docs_text = Text.objects.get(name=DOCS_NAME).text

        self.extra_points_keyboard = [[my_points_text],
                                      [docs_text]]




class ManagementFiller:

    def __init__(self):
        SCHEDULE_NAME = 'Main menu schedule'
        QUESTIONS_NAME = 'Main menu questions'
        NEWS_NAME = 'Main menu news'
        CONTACTS_NAME = 'Main menu contacts'
        MERCH_NAME = 'Main menu merch'
        EXTRA_POINTS_NAME = 'Main menu extra points'
        PROFILE_NAME = 'Main menu profile'

        self.schedule = Text.objects.get(name=SCHEDULE_NAME).text
        self.questions = Text.objects.get(name=QUESTIONS_NAME).text
        self.news = Text.objects.get(name=NEWS_NAME).text
        self.contacts = Text.objects.get(name=CONTACTS_NAME).text
        self.merch = Text.objects.get(name=MERCH_NAME).text
        self.extra_points = Text.objects.get(name=EXTRA_POINTS_NAME).text
        self.profile = Text.objects.get(name=PROFILE_NAME).text





class MerchMessageFiller:
    
    def __init__(self):
        START_NAME = 'Merch start message'

        self.merch_start_message = Text.objects.get(name=START_NAME).text




class ProfileMessageFiller:
    
    def __init__(self):
        START_NAME = 'Profile start message'
        REREGISTRATION_NAME = 'Profile reregistration message'
        PROFILE_TEXT_NAME = 'Profile profile text'
        FULLNAME_TEXT_NAME = 'Profile full name text'
        SPEC_TEXT_NAME = 'Profile spec text'
        GROUP_TEXT_NAME = 'Profile group text'
        SUBGROUP_TEXT_NAME = 'Profile subgroup text'

        self.start_message = Text.objects.get(name=START_NAME).text
        self.reregistration_message = Text.objects.get(name=REREGISTRATION_NAME).text
        self.fullname = Text.objects.get(name=FULLNAME_TEXT_NAME).text
        self.profile = Text.objects.get(name=PROFILE_TEXT_NAME).text
        self.spec = Text.objects.get(name=SPEC_TEXT_NAME).text
        self.group = Text.objects.get(name=GROUP_TEXT_NAME).text
        self.subgroup = Text.objects.get(name=SUBGROUP_TEXT_NAME).text


class ProfileKeyboardFiller:
    
    def __init__(self):
        PROFILE_NAME = 'Profile profile button'
        REREGISTRATION_AGREE_NAME = 'Profile reregistration agree button'
        REREGISTRATION_NAME = 'Profile reregistration button'

        self.profile_button_text = Text.objects.get(name=PROFILE_NAME).text
        self.reregistration_agree_button_text = Text.objects.get(name=REREGISTRATION_AGREE_NAME).text
        self.reregistration_button_text = Text.objects.get(name=REREGISTRATION_NAME).text