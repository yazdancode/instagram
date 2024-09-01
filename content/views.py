from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from content.models import Tag, Post
from content.serializers import (
    TagListSerializer,
    TagDetailSerializer,
    PostDetailSerializer,
)
from lib.pagination import SmallPageNumberPagination, StandardPageNumberPagination
from lib.permissions import RelationExists


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
    pagination_class = SmallPageNumberPagination


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


class UserPostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    lookup_url_kwarg = "user_id"
    serializer_class = PostDetailSerializer
    pagination_class =StandardPageNumberPagination
    permission_classes = [IsAuthenticated, RelationExists]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user_id=self.kwargs[self.lookup_url_kwarg])
