from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from activity.models import Comment
from content.serializers import PostDetailSerializer

User = get_user_model()


class CommentCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ("caption", "post", "reply_to", "user")
        extra_kwargs = {"reply_to": {"required": False}}

    def validate(self, attrs):
        if len(attrs["caption"]) > 30:
            raise ValidationError("Caption cannot be more than 30 characters")
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class CommentListSerializer(serializers.ModelSerializer):
    post = PostDetailSerializer()
    user = UserSerializer(read_only=True)
    replies_count = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ("id", "caption", "reply_to", "user", "post", "replies_count")

    @staticmethod
    def get_replies_count(obj):
        return obj.comment_set.count()
