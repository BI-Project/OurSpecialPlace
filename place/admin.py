from django.contrib import admin
from .models import Place, UserPlaceStar, TestPlace


admin.site.register(Place)
admin.site.register(UserPlaceStar)
admin.site.register(TestPlace)
