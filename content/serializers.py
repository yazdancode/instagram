from location.serializers import LocationSerializer
from rest_framework import serializers
from content.models import PostMedia, Tag, Post


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "title")

    def create(self, validated_data):
        instance = super().create(validated_data)
        return instance


class TagDetailSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()

    class Meta:
        model = Tag
        fields = ("id", "title", "posts")

    @staticmethod
    def get_posts(obj):
        return obj.posts.count()


class PostMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostMedia
        fields = ("id", "media_type", "media_file")


class PostDetailSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username")
    location = LocationSerializer()
    media = PostMediaSerializer(many=True)

    class Meta:
        model = Post
        fields = ("id", "caption", "user", "location", "media")
