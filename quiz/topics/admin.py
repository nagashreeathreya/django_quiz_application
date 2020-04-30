from django.contrib import admin
from .models import LoginUsers, QuizTopic


class LoginUsersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','email', 'score')


admin.site.register(LoginUsers, LoginUsersAdmin)


class QuizTopicAdmin(admin.ModelAdmin):
    list_display = ('topic_name', 'topic_code')


admin.site.register(QuizTopic, QuizTopicAdmin)
