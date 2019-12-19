from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    return HttpResponse("placeholder")

def generate_word(request):
    if "counter" not in request.session:
        request.session['counter'] = 0
    request.session['counter'] = request.session['counter'] + 1
    request.session['random_word'] = {
        "random": get_random_string(length=14),
    }
    print(request.session['random_word']['random'])
    print(f"counter = {request.session['counter']}")
    return render(request, "random_word_app/index.html")

def reset(request):
    request.session.clear()
    return redirect('/random_word')