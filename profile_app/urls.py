from django.urls import path, include
from profile_app import views

urlpatterns = [
	path('', views.p_user, name='p_user'),
	path('user_profile/', views.user_profile, name = 'user_profile'),
	path('update_profile',views.update_profile, name='update_profile'),
	path('update_kyc',views.update_kyc, name='update_kyc'),
	path('fund_request/', views.fund_request, name='fund_request'),
	path('activate_id/',views.activate_id, name='activate_id'),
	path('activate_other_id/',views.activateother_id, name='activate_other_id'),

	path('leftside_info/',views.leftside_info, name='leftside_info'),
	path('rightside_info/',views.rightside_info, name='rightside_info'),

	path('myleft_referral/',views.myleft_referral, name='myleft_referral'),
	path('myright_referral/',views.myright_referral, name='myright_referral'),

	path('matching_income/',views.matching_income, name='matching_income'),
	path('roi_income/',views.roi_income, name='roi_income'),
	path('direct_income/',views.direct_income, name='direct_income'),
	path('withrawl_income',views.withrawl_income,name='withrawl_income'),
]

