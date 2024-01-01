from django.urls import path
from userauths.views import render_login
from userauths.views import perform_login
from userauths.views import dashboard
from userauths.views import perform_logout

app_name = "userauths"

urlpatterns = [
    path("sign-up/", render_login, name="sign-up"),
    path("perform_login", perform_login, name="perform_login"),
    path("perform_logout", perform_logout, name="perform_logout"),
    path("dashboard/", dashboard, name="dashboard"),
]