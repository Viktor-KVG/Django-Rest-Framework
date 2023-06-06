from django.contrib.auth.models import User
from django.db import models


class Author(User):
    otch = models.CharField(max_length=25, verbose_name='patronymic', blank=False, )
    phone = models.CharField(max_length=12, blank=False)

    def __str__(self):
        return f"{self.username} - {self.email}"


class Coordinates(models.Model):
    latitude = models.CharField(max_length=30)
    longitude = models.CharField(max_length=30)
    height = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.latitude} / {self.longitude}'


class Level(models.Model):
    LVL = [
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D')
    ]

    STATUS = [
        ('NE', 'News'),
        ('PE', 'Pending'),
        ('AC', 'Accepted'),
        ('RE', 'Rejected')
    ]

    level_summer = models.CharField(max_length=1, verbose_name='Категория трудности (лето)', choices=LVL, )
    level_winter = models.CharField(max_length=1, verbose_name='Категория трудности (зима)', choices=LVL, )
    status_positions = models.CharField(max_length=2, verbose_name='Статус обработки',
                                        choices=STATUS, default='NE', blank=False)
    name_obj = models.CharField(max_length=250, verbose_name='Название объекта', blank=False)
    text = models.TextField(verbose_name='Текст', blank=True)
    coords = models.OneToOneField(Coordinates, verbose_name='Координаты', on_delete=models.CASCADE)
    info_author = models.ForeignKey(Author, verbose_name='Автор', on_delete=models.CASCADE, related_name='all_sync')
    add_time = models.DateTimeField(auto_now_add=True)


class Images(models.Model):
    connect_image = models.ForeignKey(Level, verbose_name='Привязать изображение к...', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    file_image = models.ImageField(verbose_name='Изображение')




