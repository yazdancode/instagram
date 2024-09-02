from django.urls import path
from content.views import TagViewSet, UserPostReadOnlyViewSet


tag_list = TagViewSet.as_view({"get": "list"})
tag_detail = TagViewSet.as_view({"get": "retrieve"})
tag_create = TagViewSet.as_view({"post": "create"})
user_post_detail = UserPostReadOnlyViewSet.as_view({"get": "retrieve"})
user_post_list = UserPostReadOnlyViewSet.as_view({"get": "list"})

urlpatterns = [
    path("tag/", tag_list, name="tags-list"),
    path("tags/create/", tag_create, name="tags-create"),
    path("tag/<int:pk>", tag_detail, name="tags-detail"),
    path("user/<str:username>/posts/", user_post_list, name="user_posts-list"),
    path(
        "user/<str:username>/posts/<int:pk>/",
        user_post_detail,
        name="user_posts-detail",
    ),
]
