from django.urls import path
from .views import VRegistro, Logout, Login

urlpatterns = [
    path('', VRegistro.as_view(), name="registro"),
    path('logout/', Logout, name="logout"),
    path('login/', Login, name="login"),
] 