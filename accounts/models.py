from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    natural_city = models.IntegerField(default=50)
    static_dynamic = models.IntegerField(default=50)
    mountain_sea = models.IntegerField(default=50)
    history_modern = models.IntegerField(default=50)
    save_flex = models.IntegerField(default=50)
    accessibility = models.IntegerField(default=50)
    dormitory_hotel = models.IntegerField(default=50)
    season = models.IntegerField(default=50)
    day_N_night = models.IntegerField(default=50)
    age = models.IntegerField(default=0)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
