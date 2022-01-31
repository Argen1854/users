from django.db import models
from django.contrib.auth.models import User


ADMIN = 1
VIP = 2
USER = 3
USER_TYPE = (
    (ADMIN, 'ADMIN'),
    (VIP, 'VIP'),
    (USER, 'USER')
)
MALE = 1
FEMALE = 2
GENDER_TYPE = (
    (MALE, 'MALE'),
    (FEMALE, 'FEMALE')
)
class CustomUser(User):

    user_type = models.IntegerField(choices=USER_TYPE, verbose_name='Тип пользователя', default=USER)
    phone_number = models.CharField(max_length=100, verbose_name='phone_number')
    age = models.IntegerField()
    country = models.CharField(max_length=100)