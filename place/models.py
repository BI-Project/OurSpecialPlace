from django.db import models


class Place(models.Model):
    place_name = models.CharField(max_length=100)
    INDOOR, OUTDOOR = 0, 1
    SPACE = (
        (INDOOR, '실내'),
        (OUTDOOR, '실외'),
    )
    space = models.SmallIntegerField(choices=SPACE)
    region = models.ForeignKey('region.Region', on_delete=models.CASCADE, related_name='place')

    def __str__(self):
        return self.place_name
