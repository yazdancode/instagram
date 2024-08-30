from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from activity.models import Comment
from content.serializers import PostDetailSerializer
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class CommentCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ("caption", "post", "reply_to", "user")
        extra_kwargs = {"reply_to": {"required": False}}

    def validate_caption(self, attr):
        if len(attr) > 30:
            raise ValidationError(_("Caption cannot be more than 30 characters"))
        return attr

    def validate_reply_to(self, attr):
        if attr.reply_to is not None:
            raise ValidationError(_("You can not reply to a reply recursively"))
        return attr

    def validate(self, attrs):
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
