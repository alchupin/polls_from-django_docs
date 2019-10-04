import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question = models.CharField(max_length=256, verbose_name='Our question')
    pub_date = models.DateTimeField(verbose_name='Publication date')

    def __str__(self):
        return self.question

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.TextField(max_length=256, verbose_name='your answer')
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

