from django.db import models
from django import forms


class Bot(models.Model):
    telegram_id = models.IntegerField(verbose_name='telegram id', null=True)
    name = models.TextField(verbose_name='имя', default='')
    nickname = models.TextField(verbose_name='username', default='')
    token = models.TextField(verbose_name='токен')

    class Meta:
        verbose_name = 'бот'
        verbose_name_plural = 'бот'

    def __str__(self):
        return f'{self.name}'


class Spec(models.Model):
    name = models.TextField(verbose_name='название')
    spec_id = models.IntegerField(verbose_name='код специальности')

    class Meta:
        verbose_name = 'специальность'
        verbose_name_plural = 'специальности'

    def __str__(self):
        return f'{self.name} ({self.spec_id})'


class Group(models.Model):
    name = models.TextField(verbose_name='название')
    spec = models.ForeignKey(Spec, verbose_name='специальность', null=True, on_delete=models.SET_NULL)
    year = models.IntegerField(verbose_name='год')
    subgroup_amount = models.IntegerField(verbose_name='количество подгрупп')
    students = models.ManyToManyField('bot.User', verbose_name='студенты', related_name='students')

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'группы'

    def __str__(self):
        return f'{self.name}'


class User(models.Model):
    telegram_id = models.IntegerField(verbose_name='telegram id', unique=True)
    telegram_name = models.TextField(verbose_name='telegram name')
    telegram_username = models.TextField(verbose_name='telegram username', null=True)
    full_name = models.TextField(verbose_name='ФИО', null=True, blank=True)
    group = models.ForeignKey(Group, verbose_name='группа', null=True, on_delete=models.SET_NULL, blank=True)
    spec = models.ForeignKey(Spec, verbose_name='специальность', null=True, on_delete=models.SET_NULL, blank=True)
    subgroup = models.IntegerField(verbose_name='подгруппа', default=0, blank=True)

    class Meta:
        verbose_name = 'юзер'
        verbose_name_plural = 'юзеры'

    def __str__(self):
        if self.full_name != None and self.group != None:
            return f'{self.full_name} {self.group}'
        elif self.full_name != None:
            return f'{self.full_name}'
        elif self.telegram_username != None:
            return f'{self.telegram_name} (@{self.telegram_username})'
        else:
            return f'{self.telegram_username}'


class Text(models.Model):
    name = models.TextField(verbose_name='имя')
    group = models.TextField(verbose_name='группа')
    text = models.TextField(verbose_name='текст')
    description = models.TextField(verbose_name='описание', null=True, blank=True)

    class Meta:
        verbose_name = 'текст'
        verbose_name_plural = 'тексты'

    def __str__(self):
        return f'Text \"{self.name}\"'


class Schedule(models.Model):
    group = models.ForeignKey(Group, verbose_name='группа', null=True, on_delete=models.SET_NULL)
    subgroup = models.IntegerField(verbose_name='подгруппа')
    schedule = models.TextField(verbose_name='расписание', null=True, blank=True)

    class Meta:
        verbose_name = 'расписание'
        verbose_name_plural = 'расписания'

    def __str__(self):
        return f'{self.group}-{self.subgroup}'


class Question(models.Model):
    sender = models.ForeignKey(User, verbose_name='отправитель', on_delete=models.SET_NULL, null=True)
    text = models.TextField(verbose_name='вопрос')
    is_answered = models.BooleanField(verbose_name='отвечен', default=False)

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'

    def __str__(self):
        return f'{self.sender} question №{self.pk}'


class Image(models.Model):
    name = models.TextField(verbose_name='название')
    description = models.TextField(verbose_name='описание', null=True, blank=True)
    image_file = models.ImageField(verbose_name='изображение', upload_to='images')

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'

    def __str__(self):
        return self.name


class Doc(models.Model):
    name = models.TextField(verbose_name='название')
    group = models.TextField(verbose_name='группа')
    description = models.TextField(verbose_name='описание')
    file = models.FileField(verbose_name='файл', upload_to='docs')

    class Meta:
        verbose_name = 'документ'
        verbose_name_plural = 'документы'

    def __str__(self):
        return self.name


class NewsCategory(models.Model):
    name = models.TextField(verbose_name='название')
    description = models.TextField(verbose_name='описание', null=True, blank=True)

    class Meta:
        verbose_name='категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return f'{self.name}'


class News(models.Model):
    name = models.TextField(verbose_name='название')
    category = models.ForeignKey(NewsCategory, verbose_name='категория', null=True, on_delete=models.SET_NULL)
    limit_date = models.DateField(verbose_name='дата завершения')
    text = models.TextField(verbose_name='текст')
    images = models.ManyToManyField(Image, verbose_name='изображения')

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'


class Event(models.Model):
    name = models.TextField('название')
    paragraph = models.TextField(verbose_name='пункт положения')
    description = models.TextField(verbose_name='описание', null=True, blank=True)
    added_date = models.DateField(verbose_name='дата добавления')
    max_points = models.IntegerField(verbose_name='максимальное количество баллов')
    actual_points = models.IntegerField(verbose_name='фактическое количество баллов')
    participants = models.ManyToManyField(User, verbose_name='студенты')

    class Meta:
        verbose_name = 'мероприятие'
        verbose_name_plural = 'мероприятия'

    def __str__(self):
        return self.name


class Merch(models.Model):
    name = models.TextField(verbose_name='название')
    description = models.TextField(verbose_name='описание', null=True, blank=True)
    images = models.ManyToManyField(Image, verbose_name='изображения')

    class Meta:
        verbose_name = 'мерч'
        verbose_name_plural = 'мерч'

    def __str__(self):
        return self.name