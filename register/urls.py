from django.urls import path
from . import views
urlpatterns = [
 path('', views.register_start, name='register'),
 path('/functions', views.functions, name='functions'),
 path('/success', views.success, name='success'),
 path('/proxy_func', views.proxy_func, name='proxy_func'),
]