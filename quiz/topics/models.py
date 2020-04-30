from django.db import models


class LoginUsers(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField()
    password = models.CharField(max_length=32)
    score = models.IntegerField(null=True, blank=True)


class QuizTopic(models.Model):
    topic_name = models.CharField(max_length=20)
    topic_code = models.CharField(max_length=10)

