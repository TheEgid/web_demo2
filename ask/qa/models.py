from __future__ import unicode_literals

from django.db import models

class Post(object):
    title = models.CharField(max_length=255)
    content = models.TextField()
    creation_date = models.DateTimeField(blank=True)
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return '/question/%d/' % self.pk

    class Meta:
        db_table = 'qa__question'
        ordering = ['-creation_date']
