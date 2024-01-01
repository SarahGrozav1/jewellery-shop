from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
# from userauths.forms import UserRegisterForm
# from django.contrib.auth import login, authenticate
# from django.contrib import messages
# from django.shortcuts import redirect

# from django.contrib.auth.views import LoginView


def render_login(request):
    return render(request, "userauths/sign-up.html/")

def perform_login(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed")
    else:
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        user_obj = authenticate(request, username=username, email=email, password1=password1, password2=password2)
        if user_obj is not None:
            login(request, user_obj)
            return HttpResponseRedirect(reverse("core/dashboard"))
        else:
            return render(request, "userauths/sign-up.html/")
        
def dashboard(request):
    return render(request, "core/dashboard.html")

def perform_logout(request):
    logout(request)
    return render(request, "userauths/sign-up.html/")

# class CustomLoginView(LoginView):
#     template_name = 'base'

# def register_view(request):

#     if request.method == "POST":
#         form = UserRegisterForm(request.POST or None)
#         if form.is_valid():
#             new_user = form.save()
#             username = form.cleaned_data.get("username")
#             messages.success(request, f'Hey {username}, your account was created successfully!')
#             new_user = authenticate(username=form.cleaned_data['email'], 
#                                     password=form.cleaned_data['password1']
#             )
#             login(request, new_user)
#             return redirect("core:index")
        
#     else:
#         form = UserRegisterForm()

#     context = {
#         'form': form,
#     }
#     return render(request, "userauths/sign-up.html", context)


