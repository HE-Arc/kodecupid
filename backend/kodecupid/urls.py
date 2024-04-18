"""
URL configuration for kodecupid project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from kodecupidapp.views import (
    UserView,
    TagView,
    PictureView,
    LikeView,
    SwipeView,
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

base_url = 'api/'

router = routers.DefaultRouter()
router.register('users', UserView, basename='user')
router.register('tags', TagView, basename='tag')
router.register('pictures', PictureView, basename='picture')
router.register('likes', LikeView, basename='like')
router.register('swipes', SwipeView, basename='swipe')

urlpatterns = [

    path('admin/', admin.site.urls),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path(base_url, include(router.urls)),
]