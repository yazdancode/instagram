from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
import debug_toolbar

# Initial urlpatterns definition
urlpatterns = [
    path("admin/", admin.site.urls),
    path("content/", include("content.urls")),
    path("activity/", include("activity.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

# Add debug toolbar URLs if in DEBUG mode
if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
