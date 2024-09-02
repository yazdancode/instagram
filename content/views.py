from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from activity.serializers import LikeSerializer
from content.models import Tag, Post
from content.serializers import (
    TagListSerializer,
    TagDetailSerializer,
    PostDetailSerializer,
)
from lib.pagination import SmallPageNumberPagination, StandardPageNumberPagination
from lib.permissions import RelationExists


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer
    permission_classes = [IsAuthenticated, RelationExists]
    pagination_class = SmallPageNumberPagination

    def retrieve(self, request, pk=None, *args, **kwargs):
        tag = get_object_or_404(Tag, pk=pk)
        serializer = TagDetailSerializer(tag)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class UserPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    lookup_url_kwarg = "pk"
    serializer_class = PostDetailSerializer
    pagination_class = StandardPageNumberPagination
    permission_classes = [IsAuthenticated, RelationExists]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user__username=self.kwargs["username"])

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, RelationExists]
        return [permission() for permission in permission_classes]
    
    def get_serializer_class(self):
        if self.action == 'get_likes_list':
            return LikeSerializer
        return self.serializer_class
    
    @action(detail=True)
    def get_likes_list(self, request, *args, **kwargs):
        post = self.get_object()
        queryset = post.likes.all()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
