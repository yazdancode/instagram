from rest_framework.permissions import BasePermission
from relation.models import Relation

class RelationExists(BasePermission):
	def  has_permission(self, request, view):
		relation_exists=Relation.objects.filter(from_user=request.user, to_user=view.kwargs['user_id']).exists()
		return relation_exists
	
	
	
