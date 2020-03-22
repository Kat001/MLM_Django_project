from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.p_user, name='p_user')
]
