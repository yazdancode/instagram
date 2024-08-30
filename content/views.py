from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from activity.models import Comment
from content.models import Tag, Post
from content.serializers import (
    TagListSerializer,
    TagDetailSerializer,
    PostDetailSerializer,
)


class TagDetailAPI(APIView):
    @staticmethod
    def get(request, pk, *args, **kwargs):
        tag = get_object_or_404(Tag, pk=pk)
        serializer = TagDetailSerializer(tag)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TagListAPI(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer
    permission_classes = (IsAuthenticated,)


class TagCreateAPIView(CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer


class PostDetailAPI(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

