
from django.http import request
from django.shortcuts import render, redirect
from .models import Trainer
from accounts.models import FitnessProfile 



def bmi(request):
    result = None
    error = None

    if request.method == 'POST':
       
       
        
            try:
                weight = float(request.POST.get('weight'))
                height = float(request.POST.get('height'))

                if height <= 0:
                    error = "Height must be greater than 0"
                else:
                    result = round(weight / (height * height), 2)
                    # print("BMI:", bmi)

            except:
                error = "Invalid input"

    return render(request, 'bmi.html', {
         'bmi': result,
        'error': error
    })


print("i am coming wait for me ")  # DEBUG



# 📄 ABOUT PAGE
def about(request):
    return render(request, 'about.html')


#  CONTACT PAGE
def contact(request):
    return render(request, 'contact.html')


# 🧪 TEST / INDEX PAGE

# def bmi(request):
#     return render(request, 'bmi.html')

def home(request):
    return render(request, 'home.html')

# blog page 
def blog(request):
    return render(request, 'blog.html')
    


# 💪 TRAINERS + SEARCH
def trainers(request):
    query = request.GET.get('q')

    if query:
        trainers = Trainer.objects.filter(name__icontains=query)
    else:
        trainers = Trainer.objects.all()

    return render(request, 'trainers.html', {
        'trainers': trainers
    })


#               assessment fitness 

def assessment (request):
    questions = [
     
        {
            # Q1
            "question": "what is your fitness goal?",
            "options": [
                "lose weight",
                "Build Muscles",
                "Get stronger",
                "Improve general fitness Level  ",
                "Improve stamina/endurance",
            ]
        },
        {
            # Q2
            "question": "How does your weight typically change?",
            "options":[
                 "I gain weight easily",
                 "I lose weight easily",
                 "My weight stays about the same",
                 "My weight changes depending on my routine",
                 "i dont gain weight at all",
            ],
        },
        
        {
            # Q3
             "question": "How active are you currently?",
             "options": [
                 "Not very active",
                 "Lightly active",
                 "Moderately active",
                 "Very active",
             ],
        },
        
        {
            # Q4
             "question": "What equipment do you have access to?",
             "options": [
                 "Gym ",
                 "Basic equipment",
                 "Full gym equipment",
                 "Home and Gym equipment",
                 "None of the above",
             ],
            
        },
        
       
        
        {
            #Q5
            "question": "Where do you prefer to work out?",
             "options": [
                 "At home",
                 "At the gym",
                 "Both home and gym",
                 "Outdoors",
                 "Dosen't workout at all"
           ],   
        },
        
        {
                    #Q6
                    "question": "How offten do you visit the gym?",
                    "options": [
                        "once in a week",
                        "very often",
                        "once in two weeks",
                        "Dosen't at all",
                        "once a month",
                    ],
                },
        
        
           {
            #Q 7
                    "question": "How often can you workout at home ?",
                     "options": [
                        "1–2 days a week",
                         "3–4 days a week",
                         "5–6 days a week",
                         "Every day",
                     ],
                },
        
        
        {
            # Q8
            "question": "How long do you want your workouts to be or do you workout?",
             "options": [
                 "15–20 minutes",
                 "30 minutes",
                 "45 minutes",
                 "60+ minutes",
                 "120+ minutes"
           ],
            
        },
        
        {
            # Q9 
             "question": "What is your current fitness level?",
             "options": [
                 "Beginner",
                 "Intermediate",
                 "Advanced",
                 "Guru",
            ],
            
        },
        
        
    ]
    
    if request.method == "POST":
        answers = {}

        for number in range(1, 10):
            answers[f"question_{number}"] = request.POST.get(
                f"question_{number}"
            )

        print("ASSESSMENT ANSWERS:", answers)

        if request.user.is_authenticated:
            FitnessProfile.objects.update_or_create(
                user=request.user,
                defaults={
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

            print("FITNESS PROFILE SAVED:", request.user.username)
        else:
            request.session["assessment_answers"] = answers
            print("GUEST ASSESSMENT SAVED TO SESSION ")

        return redirect("assessment")

    return render(
        request,
        "assessment.html",
        {"questions": questions}
    )
    
    
    
    
    
    
        
        
        
        
        
        
        
        
        
        
    
    
    # check 
    
    
    # 🧪 FITNESS ASSESSMENT
# def assessment(request):

#     questions = [
#         {
#             "question": "What is your main fitness goal?",
#             "options": [
#                 "Lose weight",
#                 "Build muscle",
#                 "Get stronger",
#                 "Improve general fitness",
#                 "Improve stamina/endurance",
#             ],
#         },

#         {
#             "question": "How does your weight typically change?",
#             "options": [
#                 "I gain weight easily",
#                 "I lose weight easily",
#                 "My weight stays about the same",
#                 "My weight changes depending on my routine",
#             ],
#         },
#         {
#             "question": "How active are you currently?",
#             "options": [
#                 "Not very active",
#                 "Lightly active",
#                 "Moderately active",
#                 "Very active",
#             ],
#         },
#         {
#             "question": "How often can you work out?",
#             "options": [
#                 "1–2 days a week",
#                 "3–4 days a week",
#                 "5–6 days a week",
#                 "Every day",
#             ],
#         },
#         {
#             "question": "Where do you prefer to work out?",
#             "options": [
#                 "At home",
#                 "At the gym",
#                 "Both home and gym",
#                 "Outdoors",
#             ],
#         },
#         {
#             "question": "How long do you want your workouts to be?",
#             "options": [
#                 "15–20 minutes",
#                 "30 minutes",
#                 "45 minutes",
#                 "60+ minutes",
#             ],
#         },
#         {
#             "question": "What is your current fitness level?",
#             "options": [
#                 "Beginner",
#                 "Intermediate",
#                 "Advanced",
#             ],
#         },
#         {
#             "question": "What equipment do you have access to?",
#             "options": [
#                 "No equipment",
#                 "Basic equipment",
#                 "Full gym equipment",
#                 "A mixture of home and gym equipment",
#             ],
#         },
#     ]

#     return render(request, "assessment.html", {
#         "questions": questions,
#     })
   

