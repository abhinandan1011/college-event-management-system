from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('events/<str:category>/', views.event_list, name='event_list'),
    path('logout/', views.logout_view, name='logout'),
]
