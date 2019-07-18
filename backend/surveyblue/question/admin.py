from django.contrib import admin
from .models import OptionResponse, Question


admin.site.register(Question)
admin.site.register(OptionResponse)
