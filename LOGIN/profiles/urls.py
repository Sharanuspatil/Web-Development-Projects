from django.urls import path, re_path

from .views import (
	signup,  account_activation_sent_view, account_activate
)

app_name = 'profiles'

urlpatterns = [
	path('', signup, name='profile-signup'),
	
	
]

urlpatterns += [
	path('account-activation-sent/', account_activation_sent_view, name='account-activation-sent'),
	path('activate/<uidb64>/<token>/',
		account_activate, name='activate'),
]
