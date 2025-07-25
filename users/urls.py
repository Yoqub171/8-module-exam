from django.urls import path, include
from .views import UserViewSet, RegisterViewSet, LoginViewSet, LogoutAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')

register = RegisterViewSet.as_view({'post': 'create'})
login = LoginViewSet.as_view({'post': 'create'})

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
]
