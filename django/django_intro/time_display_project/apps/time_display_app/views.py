from django.shortcuts import render, redirect
from time import strftime

# Create your views here.
def index(request):
    context = {
        "time": strftime("%b %d, %Y"),
        "date": strftime("%I:%M %p")
    }
    print(context['time'])
    return render(request, "time_display_app/index.html", context)

def time_display(request):
    return redirect('/')