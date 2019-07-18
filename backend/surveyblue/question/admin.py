from django.contrib import admin
from .models import OptionResponse, Question, Question_OptionResponse


class OptionInline(admin.TabularInline):
    model = Question_OptionResponse
    extra = 1



class QuestionAdmin(admin.ModelAdmin):
    inlines = (OptionInline, )


admin.site.register(Question, QuestionAdmin)
admin.site.register(OptionResponse)
