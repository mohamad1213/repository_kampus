from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.loginPage, name="login"),  
	path('register/', views.registerPage, name="register"),
	path('logout/', views.logoutUser, name="logout"),
	# path('reset_password/',views.ForgotPassword, name="reset_password"),
	# path('change_password/<token>',views.ChangePassword, name="change_password"),
	path('reset_password/',auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name="password_reset_complete"),
	path('change_password/',auth_views.PasswordChangeView.as_view(template_name="password_change.html"), name="change_password"),
    path('change_password_done/', auth_views.PasswordChangeDoneView.as_view(template_name="password_change_done.html"), name="password_change_done"),

	# path('password_change/', views.password_change, name="password_change"),
	# path('password_change/done/', views.password_change_done, name="password_change_done"),
	# path('password_reset/', views.password_reset, name="password_reset"),
	# path('password_reset/done/', views.password_reset_done, name="password_reset_done"),
]
