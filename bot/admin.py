from django.contrib import admin
from .models import *
from .forms import *
from django.contrib import auth


admin.site.unregister(auth.models.Group)
admin.site.unregister(auth.models.User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['telegram_id', 'telegram_name', 'telegram_username', 'full_name', 'group', 'spec', 'subgroup']
    list_filter = ['group', 'spec', 'subgroup']
    readonly_fields = ['telegram_id', 'telegram_name', 'telegram_username']
    search_fields = ['telegram_id', 'telegram_name', 'telegram_username', 'full_name', 'subgroup', 'group__name',
                     'spec__name', 'spec__spec_id']
    form = UserForm


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'spec', 'year', 'subgroup_amount']
    list_filter = ['spec', 'year', 'subgroup_amount']
    search_fields = ['name', 'year', 'subgroup_amount', 'spec__name', 'spec__spec_id']
    form = GroupForm


@admin.register(Spec)
class SpecAdmin(admin.ModelAdmin):
    list_display = ['name', 'spec_id']
    form = SpecForm


@admin.register(Bot)
class BotAdmin(admin.ModelAdmin):
    list_display = ('telegram_id', 'name', 'nickname', 'token')
    readonly_fields = ['telegram_id', 'name', 'nickname', 'token']
    form = BotForm

    def get_actions(self, request):
        return None

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'text', 'description')
    list_filter = ['group']
    readonly_fields = ['name', 'group']
    search_fields = ['name', 'group', 'text', 'description']
    form = TextForm

    def get_actions(self, request):
        return None

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('group', 'subgroup', 'schedule')
    list_filter = ['group', 'subgroup', 'group__spec']
    search_fields = ['group__name', 'subgroup', 'group__spec']
    form = ScheduleForm


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('sender', 'is_answered', 'text')
    list_filter = ['is_answered']
    readonly_fields = ['sender', 'text']
    search_fields = ['sender__full_name', 'sender__telegram_id', 'sender__telegram_name', 'sender__telegram_username',
                     'sender__group__name', 'sender__spec__name', 'sender__subgroup', 'text']
    form = QuestionForm


@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    form = NewsCategoryForm


class NewsImagesInline(admin.TabularInline):
    model = News.images.through
    verbose_name = 'изображение'
    verbose_name_plural = 'изображения'



@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'limit_date', 'text')
    list_filter = ['category']
    inlines = [NewsImagesInline]
    search_fields = ['name', 'limit_date', 'category__name', 'text']
    form = NewsForm


class ParticipantsInline(admin.TabularInline):
    model = Event.participants.through
    verbose_name = 'участник'
    verbose_name_plural = 'участники'


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'paragraph', 'added_date', 'description', 'max_points', 'actual_points')
    inlines = [ParticipantsInline]
    search_fields = ['name', 'paragraph', 'added_date', 'description', 'max_points', 'actual_points']
    form = EventForm


class MerchImagesInline(admin.TabularInline):
    model = Merch.images.through
    verbose_name = 'изображение'
    verbose_name_plural = 'изображения'


@admin.register(Merch)
class MerchAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [MerchImagesInline]
    form = MerchForm


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image_file')
    search_fields = ['name', 'description']
    form = ImageForm


@admin.register(Doc)
class DocAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'description', 'file')
    list_filter = ['group']
    form = DocForm