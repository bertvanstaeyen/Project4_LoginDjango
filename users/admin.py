from django.contrib import admin
from .models import Profile, WimhElectricity, SerialNumber

admin.site.register(Profile)
admin.site.register(WimhElectricity)
admin.site.register(SerialNumber)
