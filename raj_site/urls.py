from django.contrib import admin
from django.urls import path, include
from user_app import views as user_views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

from admin_panel import views as admin_views


urlpatterns = [

	path('admin_panel/send_funds/update_funds/<str:user_name>/<int:fund>/<int:i_d>/',admin_views.update_funds),

	path('admin/', admin.site.urls),
	path('', include('home_app.urls')),
	path('p/',include('profile_app.urls')),

	path('admin_panel/',include('admin_panel.urls')),


	path('signup/', user_views.register, name='register'),
	path('login/', auth_views.LoginView.as_view(template_name='user_templates/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='user_templates/logout.html'),name='logout'),
	

	path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='user_templates/password_reset.html'), name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='user_templates/password_reset_done.html'), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name='user_templates/password_reset_confirm.html'), name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='user_templates/password_reset_complete.html'), name='password_reset_complete'),

]



if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)