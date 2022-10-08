from rest_framework import serializers
from django.conf import settings
from .models import Postit

MAX_POST_LENGTH = settings.MAX_POST_LENGTH


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postit
        fields = ['content']

    def validate_content(self, value):
        if len(value) > MAX_POST_LENGTH:
            raise serializers.ValidationError("This message is too long")
        return value
