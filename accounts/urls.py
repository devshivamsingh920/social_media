from django.urls import path
from .views import RegisterView,LoginAPIView,ProfileAPIView,UpdateProfileAPIView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('profile/', ProfileAPIView.as_view(), name='profile'),
    path('profile/update/', UpdateProfileAPIView.as_view(), name='update-profile'),
]
