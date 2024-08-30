from rest_framework import serializers
from content.models import PostMedia, Tag, Post


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "title")


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
    location = serializers.SerializerMethodField()
    media = PostMediaSerializer(many=True)
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ("id", "caption", "user", "location", "media", "comments")

    def get_location(self, obj):
        from location.serializers import LocationSerializer

        return LocationSerializer(obj.location).data

    def get_comments(self, obj):
        from activity.serializers import CommentListSerializer

        serializer = CommentListSerializer(
            obj.comments.filter(reply_to__isnull=True), many=True
        )
        return serializer.data
