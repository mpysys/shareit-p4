from rest_framework import serializers
from django.conf import settings
from .models import Postit

MAX_POST_LENGTH = settings.MAX_POST_LENGTH
POST_ACTION_OPTIONS = settings.POST_ACTION_OPTIONS

class PostActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()

    def validate_action(self, value):
        value = value.lower().strip()
        if not value in POST_ACTION_OPTIONS:
            raise serializers.ValidationError("This action does not work for posts")
        return value

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postit
        fields = ['content']

    def validate_content(self, value):
        if len(value) > MAX_POST_LENGTH:
            raise serializers.ValidationError("This message is too long")
        return value
