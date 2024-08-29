from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from activity.models import Comment
from activity.serializers import CommentCreateSerializer, CommentListSerializer

class CommentListCreateAPIView(ListCreateAPIView):
    queryset = Comment.objects.filter(reply_to__isnull=True)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CommentListSerializer
        return CommentCreateSerializer


class CommentRetrieveAPIView(RetrieveUpdateAPIView):
    queryset = Comment.objects.filter(reply_to__isnull=True)
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CommentListSerializer
        return CommentCreateSerializer

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
