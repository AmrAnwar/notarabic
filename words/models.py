from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.

class Word(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="word_creator"
                             )
    name = models.CharField(max_length=50, null=False)
    description = models.TextField()
    example = models.TextField(null=True, blank=True)
    # ToDo add image field
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class WordTimeStamp(models.Model):
    word = models.ForeignKey(Word,
                             on_delete=models.CASCADE,
                             related_name="word"
                             )
    location = models.CharField(max_length=50, null=False)
    created_at = models.DateField()

    # ToDo add methods field
    @property
    def today_count(self):
        word_query = WordTimeStamp.objects.filter(word=self.word)
        count = word_query.filter(created_at__gte=datetime.date.today()).count()
        return count

    @property
    def genral_count(self):
        return WordTimeStamp.objects.filter(word=self.word).count()

    def __str__(self):
        return self.word.name
