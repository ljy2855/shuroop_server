from django.contrib import admin
from . import models


admin.site.register(models.Position)
admin.site.register(models.Place)
admin.site.register(models.Record)

# Register your models here.
