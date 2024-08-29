from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from activity.models import Comment
from activity.serializers import CommentCreateSerializer


class CommentCreateAPIView(CreateAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentCreateSerializer
	