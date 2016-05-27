from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from datetime import datetime

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-id')
    def popular(self):
        return self.order_by('-rating')

class Question(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    added_at = models.DateTimeField(default=datetime.now())
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='set_qlikes')
    objects = QuestionManager()

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(default=datetime.now())
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, blank=True, null=True)
