from django.db import models

from django.contrib.auth.models import User


class Post(models.Model):
    """Статьи"""
    author = models.ForeignKey(User, verbose_name = 'Автор', on_delete=models.CASCADE)
    title = models.CharField('Статья', max_length=100, blank=True, default='')
    body = models.TextField('Содержание', blank=True, default='')
    created_at = models.DateTimeField('Создана', auto_now_add=True)
    updated_at = models.DateTimeField('Изменена', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    """Комментарий к статье"""

    MIN_RATING = 1
    MAX_RATING = 5
    
    created = models.DateTimeField(auto_now_add=True)
    comment = models.TextField('Комментарий', blank=False)
    created_at = models.DateTimeField('Создан', auto_now_add=True)
    author = models.ForeignKey(User, verbose_name = 'Автор', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name = 'Статья', related_name='comments', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField('Оценка')
    
    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Category(models.Model):
    """Категория статьи"""
    name = models.CharField('Категория', max_length=100, blank=False, default='')
    author = models.ForeignKey(User, verbose_name = 'Автор', related_name='categories', on_delete=models.CASCADE)
    post = models.ManyToManyField(Post, verbose_name = 'Статья', related_name='categories', blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
