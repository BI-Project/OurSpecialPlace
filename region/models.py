from django.db import models


class Region(models.Model):
    region_name = models.CharField(max_length=5)

    def __str__(self):
        return self.region_name