from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime
from django.forms import ModelForm
from django.core.exceptions import NON_FIELD_ERRORS


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    choice_text = models.CharField(max_length=200, default="")
    votes = models.IntegerField(default=0)

    def __str__(self):
        #return self.question_text + " " + self.choice_text + " " + str(self.votes)
        return str(self.pub_date)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - timezone.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

"""
class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
"""