from django.urls import path, include
from rest_framework.routers import SimpleRouter
from content.views import TagViewSet, UserPostViewSet
router = SimpleRouter()
router.register('post', UserPostViewSet, 'user-post')
urlpatterns = [
    path('tags/', TagViewSet.as_view({'get':'list'}), name ='tags-list'),
    path('tags/create/', TagViewSet.as_view({'get':'create'}), name='tags-create'),
    path('tag/<int:pk>/', TagViewSet.as_view({'get':list}), name='tags-detail'),
    path('user/<str:username>/', include(router.urls)),
]
