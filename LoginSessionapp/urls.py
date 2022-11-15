from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),   
    path("visit-count/", views.visit_count, name="visit-count"),
    path("clear-count/", views.clear_count, name="clear-count"),
    path("login/", views.login, name="login"),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.logout, name="logout"),
]