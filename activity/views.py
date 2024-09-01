from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView, RetrieveAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from activity.models import Comment, Like
from activity.serializers import CommentCreateSerializer, CommentListSerializer, PostLikeSerializer
from lib.permissions import HasPostPermission


class CommentListCreateAPIView(CreateAPIView):
    queryset = Comment.objects.filter(reply_to__isnull=True)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CommentListSerializer
        return CommentCreateSerializer

class LikeCreateAPIView(RetrieveAPIView):
    queryset = Like.objects.all()
    serializer_class = PostLikeSerializer
    permission_classes = [IsAuthenticated, HasPostPermission]
    
    def post(self, request, pk, *args, **kwargs):
        object =self.get_object()
        # Todo: Store Like record
        return Response()
        

class CommentRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CommentListSerializer
        return CommentCreateSerializer

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
