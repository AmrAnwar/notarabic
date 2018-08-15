from rest_framework import serializers

from .models import GeneralWord, UserWord

class UserWordSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserWord
        fields = [
            'id',
            'user',
            'description',
            'example',
            'up_vote',
            'down_vote',
        ]

class GeneralWordSerializer(serializers.HyperlinkedModelSerializer):

    words = UserWordSerializer(many=True)
    class Meta:
        model = GeneralWord
        fields = [
            'id',
            'name',
            'words',
        ]


class SimpleGeneralWordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GeneralWord
        fields = [
            'id',
            'name',
        ]
