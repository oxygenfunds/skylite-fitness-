from django.shortcuts import render
from django.contrib.auth.models import User 
from django.contrib import messages 
from django.shortcuts import redirect 
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout 

# Create your views here.
def signin (request):
     return render(request, "signin.html")
 
def signup  (request):
     return render(request, "signup.html")
 
@login_required
def dashboard (request):
     return render(request, "dashboard.html")
 
# def logout_user(request):
#     pass 
def logout_user(request): 
    logout(request)
    return redirect("home")
 

def signin(request):
    
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )
        # if password = lessthanI(8) 
        #  return Error(" password must be at least 8")

        if user is not None:

            login(request, user)

            return redirect("dashboard")

        else:

            messages.error(
                request,
                "Invalid username or password."
            )

            return redirect("signin")

    return render(request, "signin.html")