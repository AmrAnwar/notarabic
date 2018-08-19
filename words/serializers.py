from rest_framework import serializers

from .models import GeneralWord, UserWord, WordTimeStamp

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

class WordTimeStampSerializer(serializers.ModelSerializer):
    word = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = WordTimeStamp
        fields = ['today_count',
                  'general_count',
                  'word'
                ]

class GeneralWordSerializer(serializers.HyperlinkedModelSerializer):

    words = UserWordSerializer(many=True)


    class Meta:
        model = GeneralWord
        fields = [
            'id',
            'name',
            'general_count',
            'today_count',
            'words',


        ]



class SimpleGeneralWordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GeneralWord
        fields = [
            'id',
            'name',
        ]
