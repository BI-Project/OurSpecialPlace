from django.db import models


class Place(models.Model):
    picture = models.ImageField(blank=True, upload_to='img')
    name = models.CharField(max_length=100)
    natural_city = models.IntegerField(default=0)
    static_dynamic = models.IntegerField(default=0)
    mountain_sea = models.IntegerField(default=0)
    history_modern = models.IntegerField(default=0)
    save_flex = models.IntegerField(default=0)
    accessibility = models.IntegerField(default=0)
    dormitory_hotel = models.IntegerField(default=0)
    season = models.IntegerField(default=0)
    day_N_night = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    comment = models.TextField()
    star = models.IntegerField(default=0)
    liked_user = models.ManyToManyField('accounts.User', blank=True, related_name='place')

    def __str__(self):
        return self.name
