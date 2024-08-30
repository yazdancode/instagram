from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView, DestroyAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from activity.models import Comment
from activity.serializers import CommentCreateSerializer, CommentListSerializer


class CommentListCreateAPIView(CreateAPIView):
    queryset = Comment.objects.filter(reply_to__isnull=True)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CommentListSerializer
        return CommentCreateSerializer


class CommentRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CommentListSerializer
        return CommentCreateSerializer

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
