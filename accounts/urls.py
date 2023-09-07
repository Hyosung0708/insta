from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('search/', views.search_profile, name='search_profile'),
    path('<str:username>/', views.profile, name='profile'),
    path('<str:username>/follow/', views.follow, name='follow'),
    path('search/<str:username>/', views.search_profile, name='search_profile')
    
]