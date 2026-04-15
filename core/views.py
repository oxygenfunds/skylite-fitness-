
from django.shortcuts import render
from .models import Trainer




def bmi(request):
    bmi = None
    error = None

    if request.method == 'POST':
        try:
            weight = float(request.POST.get('weight'))
            height = float(request.POST.get('height'))

            if height <= 0:
                error = "Height must be greater than 0"
            else:
                bmi = round(weight / (height * height), 2)

        except (ValueError, TypeError):
            error = "Please enter valid numbers"

    return render(request, 'index.html', {
        'bmi': bmi,
        'error': error
    })
    



# 📄 ABOUT PAGE
def about(request):
    return render(request, 'about.html')


#  CONTACT PAGE
def contact(request):
    return render(request, 'contact.html')


# 🧪 TEST / INDEX PAGE
def bmi(request):
    return render(request, 'index.html')

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


