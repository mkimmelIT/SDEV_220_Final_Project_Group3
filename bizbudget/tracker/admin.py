from django.contrib import admin
from .models import Tracker
from .models import Requester

admin.site.register(Tracker)
admin.site.register(Requester)
