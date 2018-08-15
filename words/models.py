import datetime

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class GeneralWord(models.Model):
    # TODO check max_length
    name = models.CharField(max_length=300, null=False, blank=False, unique=True)
    words = models.ManyToManyField("words.UserWord")
    created_at = models.DateField(auto_now_add=True)

    # def __str__(self):
    #     return self.name

class UserWord(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="word_creator"
                             )
    up_vote = models.ManyToManyField(User, related_name="up_vote",null=True,blank=True)
    down_vote = models.ManyToManyField(User, related_name="down_vote",null=True,blank=True)

    description = models.TextField()
    example = models.TextField(null=True, blank=True)
    # ToDo add image field
    created_at = models.DateField(auto_now_add=True)

    # TODO
    # def __str__(self):

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        return super(UserWord, self).save(
            force_insert=False,
            force_update=False,
            using=None,
            update_fields=None)

    def delete(self, using=None, keep_parents=False):
        return super(UserWord, self).delete(
            using=None,
            keep_parents=False,
        )

class WordTimeStamp(models.Model):
    """
    created after each request to word page
    """
    word = models.ForeignKey(GeneralWord,
                             on_delete=models.CASCADE,
                             related_name="general_word"
                             )
    location = models.CharField(max_length=50, null=False)
    created_at = models.DateField()

    # ToDo add methods field
    @property
    def today_count(self):
        word_query = WordTimeStamp.objects.filter(word=self.word)
        # edited by amr: remove __gte
        count = word_query.filter(created_at=datetime.date.today()).count()
        return count

    @property
    def genral_count(self):
        return WordTimeStamp.objects.filter(word=self.word).count()

    def __str__(self):
        return self.word.name
