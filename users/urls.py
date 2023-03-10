from django.urls import path, include

from users.apps import UsersConfig
from users.views import UserRegister

app_name = UsersConfig.name

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', UserRegister.as_view(), name='register'),

]
