from django.shortcuts import render

from django.http import HttpResponse

from .models import Myreg

# Create your views here.


def index(request):
    

    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        gender = request.POST['gender']
        num = request.POST['num']
        location = request.POST['location']
        email = request.POST['email']

        reg = Myreg(
            fname = fname,
            lname = lname,
            gender = gender,
            whatsapp = num,
            location = location,
            email = email
        )
        reg.save()
    
        return render(request, "smartcode/message.html")
    return render(request, 'smartcode/index.html')

def message(request):
    return render(request, 'smartcode/message.html')