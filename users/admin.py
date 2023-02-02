from django.contrib import admin
from .models import Profile, WimhElectricity, SerialNumber

# admin can access data by going to /admin
# admin can see this data
# used for testing, not deployement
admin.site.register(Profile)
admin.site.register(WimhElectricity)
admin.site.register(SerialNumber)
