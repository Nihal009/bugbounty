from django.urls import path
from . import views

urlpatterns = [
     # path('signup/', views.user_signup, name='user_signup'),
     # path('login/',views.user_login,name='user_login'),
     path('auth/',views.user_auth_page,name='user_auth'),
     path('dashboard/',views.user_dashboard,name='user_dashboard'),
     path('programs/<int:id>/', views.program_detail, name='program_detail'),
]