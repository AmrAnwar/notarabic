# Generated by Django 2.1 on 2018-08-15 16:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0002_auto_20180815_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userword',
            name='down_vote',
            field=models.ManyToManyField(blank=True, null=True, related_name='down_vote', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userword',
            name='up_vote',
            field=models.ManyToManyField(blank=True, null=True, related_name='up_vote', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='wordtimestamp',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
