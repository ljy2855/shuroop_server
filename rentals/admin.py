from django.contrib import admin
from . import models


admin.site.register(models.Position)
admin.site.register(models.Place)
admin.site.register(models.Record)
admin.site.register(models.CurrentSearchPlace)
admin.site.register(models.FavoritePlace)

# Register your models here.
