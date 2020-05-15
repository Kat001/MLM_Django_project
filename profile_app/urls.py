from django.urls import path, include
from profile_app import views

urlpatterns = [
	path('', views.p_user, name='p_user'),
	path('fund_request/', views.fund_request, name='fund_request'),
	path('activate_id/',views.activate_id, name='activate_id'),
	path('activate_other_id',views.activateother_id, name='activate_other_id')
]
