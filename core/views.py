
from django.shortcuts import render
from .models import Trainer




# def bmi(request):
#     bmi = None
#     error = None

#     if request.method == 'POST':
#         print("POST request received")
#         try:
#             weight = float(request.POST.get('weight'))
#             height = float(request.POST.get('height'))

#             if height <= 0:
#                 error = "Height must be greater than 0"
#             else:
#                 bmi = round(weight / (height * height), 2),

#         except (ValueError, TypeError):
#             error = "Please enter valid numbers"

#     return render(request, 'index.html', {
#         'bmi': bmi,
#         'error': error,
#         'test': 'THIS IS THE REAL TEST VALUE '
#     })
    


# def bmi(request):
#     bmi = None
#     error = None

#     print("REQUEST METHOD:", request.method)  # DEBUG

#     if request.method == 'POST':
#         print("POST HIT ✅")

#         try:
#             weight = request.POST.get('weight')
#             height = request.POST.get('height')

#             print("RAW:", weight, height)

#             weight = float(weight)
#             height = float(height)

#             bmi = round(weight / (height * height), 2)

#             print("BMI CALCULATED:", bmi)

#         except Exception as e:
#             print("ERROR:", e)
#             error = "Invalid input"

#     return render(request, 'index.html', {
#         'bmi': bmi,
#         'error': error
#     })

# def bmi(request):
#     bmi = None
#     error = None

#     if request.method == 'POST':
#         print("POST HIT ✅")

#         weight = request.POST.get('weight')
#         height = request.POST.get('height')

#         print("RAW:", weight, height)

#         if not weight or not height:
#             error = "All fields are required"
#         else:
#             try:
#                 weight = float(weight)
#                 height = float(height)

#                 if height <= 0:
#                     error = "Height must be greater than 0"
#                 else:
#                     bmi = round(weight / (height * height), 2)
#                     print("BMI:", bmi)

#             except:
#                 error = "Invalid input"

#     return render(request, 'index.html', {
#         'bmi': bmi,
#         'error': error
#     })



def bmi(request):
    result = None
    error = None

    if request.method == 'POST':
       
        # weight = request.POST.get('weight')
        # height = request.POST.get('height')

        # print("RAW:", weight, height) 
        
        # if request.method == 'POST':
            
        # if not weight or not height:
        #     error = "All fields are required"
        # else:
        
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
def bmi(request):
    return render(request, 'bmi.html')

def home(request):
    return render(request, 'home.html')
    


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


