from django.urls import path

from content.views import (
    TagListAPI,
    TagDetailAPI,
    TagCreateAPIView,
    UserPostReadOnlyViewSet,
)

user_post_detail = UserPostReadOnlyViewSet.as_view({"get": "retrieve"})
user_post_list = UserPostReadOnlyViewSet.as_view({"get": "list"})
urlpatterns = [
    path("tag/", TagListAPI.as_view(), name="tags-list"),
    path("tags/create/", TagCreateAPIView.as_view(), name="tags-create"),
    path("tag/<int:pk>", TagDetailAPI.as_view(), name="tags-detail"),
    path("user/<str:username>/posts/", user_post_list, name="user_posts-list"),
    path(
        "user/<str:username>/posts/<int:pk>/",
        user_post_detail,
        name="user_posts-detail",
    ),
]
