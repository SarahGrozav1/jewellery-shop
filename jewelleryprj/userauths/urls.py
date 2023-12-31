from django.urls import path
from userauths import views

app_name = "userauths"

urlpatterns = [
    path("sign-up/", views.render_login, name="sign-up"),
    path("perform_login", views.perform_login, name="perform_login"),
    path("perform_logout", views.perform_logout, name="perform_logout"),
    path("dashboard/", views.dashboard, name="dashboard"),

]