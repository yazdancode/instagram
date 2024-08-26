from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from content.models import Tag

class TagDetailAPI(APIView):
    """
    Retrieve, update or delete a tag instance.
    """
    @staticmethod
    def get(request, pk, *args, **kwargs):
        """
        Retrieve a tag by its ID.
        """
        tag = get_object_or_404(Tag, pk=pk)
        return Response({
            'id': tag.id,
            'title': tag.title,
            'posts': tag.posts.count()
        }, status=status.HTTP_200_OK)
    
    # Optional: Implement PUT method if needed
    # def put(self, request, pk, *args, **kwargs):
    #     pass
    
    # Optional: Implement DELETE method if needed
    # def delete(self, request, pk, *args, **kwargs):
    #     pass

class TagListAPI(APIView):
    """
    List all tags or create a new tag.
    """
    @staticmethod
    def get(request, *args, **kwargs):
        """
        List all tags.
        """
        tags = Tag.objects.all()
        data = [
            {
                'id': tag.id,
                'title': tag.title,
                'posts': tag.posts.count(),
            }
            for tag in tags
        ]
        return Response(data, status=status.HTTP_200_OK)
    
    # Optional: Implement POST method if needed
    # def post(self, request, *args, **kwargs):
    #     pass
    
    # Optional: Implement PUT method if needed
    # def put(self, request, *args, **kwargs):
    #     pass
    
    # Optional: Implement DELETE method if needed
    # def delete(self, request, *args, **kwargs):
    #     pass
