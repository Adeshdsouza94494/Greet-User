from django.shortcuts import render
from datetime import datetime

# Create your views here.

def home(request):
    date=datetime.now()
    message="Hello Guest !! very Good "
    hour=int(date.strftime("%H"))
    if(hour<12):
        message+="Morning "
    elif(hour<16):
        message+="Afternoon "
    else:
        message+="Evening "


    return render(request,'home.html',{"message":message})
