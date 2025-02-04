# Приложение Нiker
## Описание приложения:
Приложение для любителей походов и покорителей новых горных вершин.
Существует для фиксирования своих подъемов, описании места ,добавления фотографий объекта и фиксации координат. Чтобы пользователи этого приложения могли делиться с друг другом местами своих побед.

>Адрес:  https://Viteeek.pythonanywhere.com
___
Установите Django, RestFramework, django-filter
```
pip install django
pip install djangorestframework
pip install django-filter
```

Настройка Setting.py

Установите и добавьте два приложения('rest_framework','django_filters')
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'testy',
]
```
Добавьте переменную фильтрации, пагинации и аутентификации
```python
REST_FRAMEWORK = {
   'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
   'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
   'PAGE_SIZE': 5,
   'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated',]
}
```
>>>Работа приложения. 
**Выберите категорию:**
 
- [x] Для начала пройдите легкую регистрацию и добавьте себя как автора.
 
- [x] Вы можете добавить свои координаты места нахождения и высоту вершины на которой находитесь
 
- [x] Дать название объекту и сделать его описание
- [x] Выбрать категории сложности восхождения на вершины  в летнее и зимнее  время.
 
- [x] Добавлять фотографии объекта и описание к ним.
 

 Все записи сохраняются в базу данных.
Поиск данных в базе вы можете произвести с помощью кнопки фильтрации на странице приложения. :wrench:
 

