from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from content.models import Tag

class TagDetailAPI(APIView):
	@staticmethod
	def get(request,pk, *args, **kwargs):
		tags =Tag.objects.filter(pk=pk)
		if not tags.exists():
			return Response('Not found', status=status.HTTP_404_NOT_FOUND)
		tag =tags.first()
		
		return Response({
					'id':tag.id,
					'title':tag.title,
					'posts':tag.posts.count()
		}, status=status.HTTP_200_OK)
	
class TagListAPI(APIView):
	@staticmethod
	def get(request, *args, **kwargs):
		tags =Tag.objects.all()
		data = list()
		for tag in tags:
			data.append(
				{
					'id':tag.id,
					'title':tag.title,
					'posts':tag.posts.count(),
				}
			)
		
		return Response(data, status=status.HTTP_200_OK)
	
	def post(self, request, *args, **kwargs):
		pass
	
	def put(self, request, *args, **kwargs):
		pass
	
	def delete(self, request, *args, **kwargs):
		pass
	
	
