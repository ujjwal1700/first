from register_app import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns=[
   path('',views.register,name="register"),
   path('login/',auth_views.LoginView.as_view(template_name='register_app/login.html',redirect_authenticated_user=True),name="login"),
   path('logout/',auth_views.LogoutView.as_view(template_name='register_app/logout.html'),name="logout"),


]
