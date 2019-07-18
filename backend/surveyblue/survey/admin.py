from django.contrib import admin

from .models import Survey, Survey_Question, Answer


class OptionInline(admin.TabularInline):
    model = Survey_Question
    extra = 1


class SurveyAdmin(admin.ModelAdmin):

    inlines = (OptionInline,)

admin.site.register(Survey, SurveyAdmin)
admin.site.register(Answer)
