from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework.permissions import BasePermission
from relation.models import Relation

User = get_user_model()


class RelationExists(BasePermission):
    """
    Checks if the user has a relation with the specified account.

    Parameters:
    - request (django.http.HttpRequest): The HTTP request object containing the user's information.
    - view (rest_framework.views.APIView): The API view object representing the endpoint where the action is being performed.

    Returns:
    - bool: Returns True if the user has a relation with the specified account, False otherwise.

    The function first retrieves the user object based on the 'user_id' provided in the view's kwargs. If a user is found, it then checks if the current user (from the request) has a relation with the specified user. This is done by querying the Relation model for entries where the 'from_user' is the current user and the 'to_user' is the specified user. If such a relation exists, or if the current user is the same as the specified user, the function returns True, indicating that the user has a relation with the specified account. Otherwise, it returns False, indicating that the user does not have a relation with the specified account.
    """
    def has_permission(self, request, view):
        user = User.objects.filter(id=view.kwargs["user_id"]).first()
        if user:
            return (
                Relation.objects.filter(from_user=request.user, to_user=user).exists()
                | request.user
                == user
            )
        return False


class HasPostPermission(BasePermission):
    """
    Checks if the user has permission to perform an action on a specific post.

    Parameters:
    - request (django.http.HttpRequest): The HTTP request object containing the user's information.
    - view (rest_framework.views.APIView): The API view object representing the endpoint where the action is being performed.
    - obj (relation.models.Post): The specific post object that the user is trying to perform an action on.

    Returns:
    - bool: Returns True if the user has permission to perform the action on the post, False otherwise.

    The function checks if the user has a relation with the post's author or if the user is the author of the post. If either condition is met, the function returns True, indicating that the user has permission to perform the action. Otherwise, it returns False, indicating that the user does not have permission.
    """
    def has_object_permission(self, request, view, obj):
        return (
            Relation.objects.filter(from_user=request.user, to_user=obj.user).exists()
            | request.user
            == obj.user
        )
