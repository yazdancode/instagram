from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from activity.models import Comment
from activity.serializers import CommentCreateSerializer, CommentListSerializer


class CommentListCreateAPIView(ListCreateAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentCreateSerializer
	permission_classes = (IsAuthenticated, )
	
	def perform_create(self, serializer):
		serializer.save(user=self.request.user)
		
		
	def get_serializer_class(self, *args, **kwargs):
		if self.request.methode == "GET":
			return CommentListSerializer
		return self.serializer_class
        
	