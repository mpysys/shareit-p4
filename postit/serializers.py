from rest_framework import serializers
from django.conf import settings
from .models import Postit

MAX_POST_LENGTH = settings.MAX_POST_LENGTH
POST_ACTION_OPTIONS = settings.POST_ACTION_OPTIONS


class PostActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()
    content = serializers.CharField(allow_blank=True, required=False)

    def validate_action(self, value):
        value = value.lower().strip()
        if value not in POST_ACTION_OPTIONS:
            raise serializers.ValidationError(
                                              "This action does" +
                                              "not work for posts"
                                              )
        return value


class PostCreateSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Postit
        fields = ['id', 'content', 'likes']

    def get_likes(self, obj):
        return obj.likes.count()

    def validate_content(self, value):
        if len(value) > MAX_POST_LENGTH:
            raise serializers.ValidationError("This message is too long")
        return value

# Read Only serializer
class PostSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    og_post = PostCreateSerializer(source='parent', read_only=True)
    class Meta:
        model = Postit
        fields = ['id', 'content', 'likes', 'is_share' , 'og_post']

    def get_likes(self, obj):
        return obj.likes.count()


