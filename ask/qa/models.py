from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import random
from django.urls import reverse


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    objects = QuestionManager()

    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes_user')
    slug = models.SlugField(verbose_name='URL', default=1, max_length=50, unique=False, )


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    question = models.ForeignKey(Question, related_name='answer_set', default=1, blank=False, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

