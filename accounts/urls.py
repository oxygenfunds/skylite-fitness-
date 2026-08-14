from django.urls import path 
from . import views 

# urlpatterns = [
#     path("signin/", views.signin, name="signin"),
#     path("signup/", views.signup, name="signup"),
#     path("logout/", views.logout_view, name="logout"),
#     path("dashboard/", views.dashboard, name="dashboard"),
# ]

urlpatterns = [
    path("signin/", views.signin, name="signin"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout_user, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
