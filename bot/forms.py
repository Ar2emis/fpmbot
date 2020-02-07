from django import forms
from .models import *




class UserForm(forms.ModelForm):

    class Meta:
        model = User

        fields = ('telegram_id', 'telegram_name', 'telegram_username', 'full_name', 'spec', 'group', 'subgroup')

        widgets = {
            'telegram_id': forms.NumberInput,
            'full_name': forms.TextInput,
            'telegram_name': forms.TextInput,
            'telegram_username': forms.TextInput,
            'subgroup': forms.NumberInput
        }


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group

        fields = ('name', 'spec', 'year', 'subgroup_amount', 'students')

        widgets = {
            'name': forms.TextInput,
            'year': forms.NumberInput,
            'subgroup_amount': forms.NumberInput,
            'students': forms.CheckboxSelectMultiple
        }


class SpecForm(forms.ModelForm):

    class Meta:
        model = Spec

        fields = ('name', 'spec_id')

        widgets = {
            'name': forms.TextInput,
            'spec_id': forms.NumberInput
        }


class BotForm(forms.ModelForm):

    class Meta:
        model = Bot

        fields = ('telegram_id',
                  'name',
                  'nickname',
                  'token')

        widgets = {
            'telegram_id': forms.NumberInput,
            'name': forms.TextInput,
            'nickname': forms.TextInput,
            'token': forms.TextInput
        }


class TextForm(forms.ModelForm):

    class Meta:
        model = Text

        fields = ('name', 'group', 'text', 'description')

        widgets = {
            'name': forms.TextInput,
            'group': forms.TextInput
        }


class ScheduleForm(forms.ModelForm):

    class Meta:
        model = Schedule

        fields = ('group', 'subgroup', 'schedule')

        widgets = {
            'subgroup': forms.NumberInput,
            'schedule': forms.Textarea(attrs={'rows': '100', 'cols': '50'})
        }


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question

        fields = ('sender', 'is_answered', 'text')


class NewsCategoryForm(forms.ModelForm):

    class Meta:
        model = NewsCategory

        fields = ('name', 'description')

        widgets = {
            'name': forms.TextInput
        }


class NewsForm(forms.ModelForm):

    class Meta:
        model = News

        fields = ('name', 'category', 'limit_date', 'text')

        widgets = {
            'name': forms.TextInput
        }


class EventForm(forms.ModelForm):

    class Meta:
        model = Event

        fields = ('name', 'paragraph', 'added_date', 'description', 'max_points', 'actual_points')

        widgets = {
            'name': forms.TextInput({'size': '50'}),
            'paragraph': forms.Textarea({'rows': '3', 'cols': '99'}),
            'max_points': forms.NumberInput,
            'actual_points': forms.NumberInput
        }


class MerchForm(forms.ModelForm):

    class Meta:
        model = Merch

        fields = ('name', 'description')

        widgets = {
            'name': forms.TextInput
        }


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image

        fields = ('name', 'description', 'image_file')

        widgets = {
            'name': forms.TextInput
        }


class DocForm(forms.ModelForm):

    class Meta:
        model = Doc

        fields = ('name', 'group', 'description', 'file')

        widgets = {
            'name': forms.TextInput,
            'group': forms.TextInput
        }