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
from django.urls import path

from kodecupidapp.views import (
    UserView, 
    TagView,
    PictureView,
    LikeView,
    UserTagView,
    user_by_id,
    random_user
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/user/', UserView.as_view(), name='user'),
    path('api/picture/', PictureView.as_view(), name='picture'),
    path('api/tags/', TagView.as_view(), name='tag-list'),
    path('api/like/', LikeView.as_view(), name='like-create'),

    path('api/user/tags', UserTagView.as_view(), name='user-tag'),

    path('api/user/random', random_user, name='random-user'),
    path('api/user/<int:id>', user_by_id, name='user-by-id')
]