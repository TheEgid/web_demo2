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


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    #question = models.ManyToManyField(Question, related_name='answer', default=1, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Question(models.Model):
    objects = QuestionManager()

    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes_user')
    slug = models.SlugField(verbose_name='URL', default=slugify(random.randint(899, 4657)), max_length=50, unique=False, )
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)


