from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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
