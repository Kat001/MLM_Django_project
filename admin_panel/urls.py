from django.urls import path, include
from admin_panel import views

urlpatterns = [
	path('', views.admin_page, name='admin_page'),
	path('send_funds/',views.send_funds,name='send_funds'),
	#path('update_funds/<str:user_name>/<int:fund>/',views.update_funds,name='upd')
	
]
