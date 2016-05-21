import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    """
    Each field is represented by an instance of a Field class
    – e.g., CharField for character fields and DateTimeField for datetime.
    This tells Django what type of data each field holds.
    The name of each Field instance (e.g. question_text or pub_date) is the field’s name

    You can use an optional first positional argument to a Field to designate a human-readable name.
    That’s used in a couple of introspective parts of Django, and it doubles as documentation.
    If this field isn’t provided, Django will use the machine-readable name.
    In this example, we’ve only defined a human-readable name for Question.pub_date.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text