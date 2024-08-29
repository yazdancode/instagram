from django.shortcuts import render
from rest_framework.decorators import permission_classes
from rest_framework.generics import CreateAPIView
from rest_framework.settings import perform_import

from activity.models import Comment
from activity.serializers import CommentCreateSerializer


class CommentCreateAPIView(CreateAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentCreateSerializer
    
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
	