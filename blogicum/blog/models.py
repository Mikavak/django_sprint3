from django.contrib.auth import get_user_model
from django.db import models

from blog.constant import MAX_CHARFIELD_LENGHT
from core.models import BaseModel


User = get_user_model()


class Post(BaseModel):
    title = models.CharField('Заголовок', max_length=MAX_CHARFIELD_LENGHT)
    text = models.TextField('Текст')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Автор публикации',
        related_name='posts_of_this_author')
    location = models.ForeignKey(
        'Location', on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name='Местоположение',
        related_name='post_write_in_this_location')
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True, blank=False,
        verbose_name='Категория', related_name='post_of_category')
    pub_date = models.DateTimeField(
        'Дата и время публикации',
        help_text=('Если установить дату и время в будущем'
                   ' — можно делать отложенные публикации.'))

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-pub_date', ]


class Category(BaseModel):
    title = models.CharField('Заголовок', max_length=MAX_CHARFIELD_LENGHT)
    description = models.TextField('Описание')
    slug = models.SlugField(
        'Идентификатор', unique=True,
        help_text=('Идентификатор страницы для URL;'
                   ' разрешены символы латиницы, цифры,'
                   ' дефис и подчёркивание.'))

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Location(BaseModel):
    name = models.CharField(
        'Название места', max_length=MAX_CHARFIELD_LENGHT)

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name
