from django.db import models

from .Manager import UserManager
from django.contrib.auth.models import (
	AbstractBaseUser, PermissionsMixin
)
from django.conf import settings 
import jwt
from datetime import datetime, timedelta
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractBaseUser, PermissionsMixin):
    
    # Каждому пользователю нужен понятный человеку уникальный идентификатор,
    # который мы можем использовать для предоставления User в пользовательском
    # интерфейсе. Мы так же проиндексируем этот столбец в базе данных для
    # повышения скорости поиска в дальнейшем.

    first_name=models.CharField(verbose_name='Имя',max_length=150)
    phone_number = PhoneNumberField(blank=True,verbose_name = 'Номер телефона', unique=True)

    
    # Когда пользователь более не желает пользоваться нашей системой, он может
    # захотеть удалить свой аккаунт. Для нас это проблема, так как собираемые
    # нами данные очень ценны, и мы не хотим их удалять :) Мы просто предложим
    # пользователям способ деактивировать учетку вместо ее полного удаления.
    # Таким образом, они не будут отображаться на сайте, но мы все еще сможем
    # далее анализировать информацию.
    is_active = models.BooleanField(default=True)

    # Этот флаг определяет, кто может войти в административную часть нашего
    # сайта. Для большинства пользователей это флаг будет ложным.
    is_staff = models.BooleanField(default=False,verbose_name='Персонал')

    # Временная метка создания объекта.
    created_at = models.DateTimeField(auto_now_add=True)

    # Временная метка показывающая время последнего обновления объекта.
    updated_at = models.DateTimeField(auto_now=True)

    # Дополнительный поля, необходимые Django
    # при указании кастомной модели пользователя.

    # Свойство USERNAME_FIELD сообщает нам, какое поле мы будем использовать
    # для входа в систему. В данном случае мы хотим использовать почту.
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', ]

    # Сообщает Django, что определенный выше класс UserManager
    # должен управлять объектами этого типа.
    objects = UserManager()
    
    
    
    class Meta:
        ordering = ['id']
        verbose_name='Пользователи'
        verbose_name_plural='Пользователи'

    def __str__(self):
        return "{}".format(self.phone_number)

    @property
    def token(self):
        """
        Позволяет получить токен пользователя путем вызова Author.token, вместо
        user._generate_jwt_token(). Декоратор @property выше делает это
        возможным. token называется "динамическим свойством".
        """
        return self._generate_jwt_token()

    def get_full_name(self):
        """
        Этот метод требуется Django для таких вещей, как обработка электронной
        почты. Обычно это имя фамилия пользователя, но поскольку мы не
        используем их, будем возвращать username.
        """
        return self.phone_number

    def get_short_name(self):
        """ Аналогично методу get_full_name(). """
        return self.phone_number

    def _generate_jwt_token(self):
        """
        Генерирует веб-токен JSON, в котором хранится идентификатор этого
        пользователя, срок действия токена составляет 1 день от создания
        """
        dt = datetime.now() + timedelta(days=1)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%S'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token



class CheckModels(models.TextChoices):
        men = "MEN", "Мужской"
        women = "WOMEN", "Женский"

class HoursModel(models.TextChoices):
        hours = 1, "час"
        hours2 = 2, "2 часа"
        hours3 = 3, "3 часа"
        hours4 = 4, "4 часа"
        hours5 = 5, "5 часов"


class BathHouseModel(models.Model):
    number_key = models.IntegerField(default= 0, verbose_name= "Номер ключа", unique=True)
    first_name = models.CharField(max_length=255, verbose_name= 'Имя')
    date_start = models.DateTimeField(auto_now_add=True, verbose_name='Время начало')
    number_phone = PhoneNumberField(verbose_name='Номер телефона')
    my_type = models.CharField(max_length=5,verbose_name='Пол', choices=CheckModels.choices, null=False, blank=False)
    hours = models.CharField(max_length=5,verbose_name='На сколько забранировано', choices=HoursModel.choices, null=False, blank=False)
    end_time = models.DateTimeField(verbose_name='Время окончания')
    
    
    def __str__(self):
        return "{}".format(self.number_key)     

    class Meta:
        ordering = ['number_key']
        verbose_name='Очередь'
        verbose_name_plural='Очередь'


