from django.contrib import admin
from .models import Tracker
from .models import TrackerUser

admin.site.register(Tracker)
admin.site.register(TrackerUser)
