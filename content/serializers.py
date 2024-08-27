from rest_framework import serializers

from content.models import Tag


class TagListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)

    def create(self, validated_data):
        instance = Tag.objects.create(**validated_data)
        return instance


class TagDetailSerializer(TagListSerializer):
    posts = serializers.SerializerMethodField()

    @staticmethod
    def get_posts(obj):
        return obj.posts.count()
