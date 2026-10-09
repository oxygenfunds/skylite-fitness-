from django.shortcuts import render
from django.contrib.auth.models import User 
from django.contrib import messages 
from django.shortcuts import redirect 
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout

from accounts.models import FitnessProfile 



def signup(request):
    
    if request.method == "POST":

        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("signup")

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("signup")

        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        answers = request.session.get("assessment_answers") 
        if answers: 
            FitnessProfile.objects.update_or_create (
                user=user,
                defaults= {
                    "Fitness_goal": answers["question_1"],
                    "weight_change": answers["question_2"],
                    "activity_level": answers["question_3"],
                    "equipment": answers["question_4"],
                    "workout_location": answers["question_5"],
                    "gym_frequency": answers["question_6"],
                    "home workout_frequency": answers["question_7"],
                    "workout_duration": answers["question_8"],
                    "Fitness_level": answers["question_9"],
                }
            )
            del request.session["assessment_answers"]
            messages.success (
                request, "Account created  please sign in to Explore your fitness journey"
            )
            
        # check for guest answers 
        answers = request.session.get("guest_answers ")
        if answers: 
            FitnessProfile.objects.update_or_create (
                user=user,
                defaults= {
            "fitness_goal": answers["question_1"],
            "weight_change": answers["question_2"],
            "activity_level": answers["question_3"],
            "equipment": answers["question_4"],
            "workout_location": answers["question_5"],
            "gym_frequency": answers["question_6"],
            "home_workout_frequency": answers["question_7"],
            "workout_duration": answers["question_8"],
            "fitness_level": answers["question_9"],
                }
            )
            del request.session["assessment_answers"]

        messages.success(
            request,
            "Account created successfully. You can now sign in."
        )

        return redirect("signin")

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