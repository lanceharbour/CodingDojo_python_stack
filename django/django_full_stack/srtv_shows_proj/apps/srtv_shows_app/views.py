from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show

# Create your views here.
def index(request):
    return redirect(f'/shows')

def shows(request):
    shows = {
        "show_list": Show.objects.all()
    }
    return render(request, "srtv_shows_app/index.html", shows)

def showInfo(request, showID):
    show_data = {
        "show_info": Show.objects.get(id=showID)
    }
    return render(request, "srtv_shows_app/show_info.html", show_data)

def newShow(request):
    return render(request, "srtv_shows_app/new_show.html") 

def addShow(request):
    if request.method == "POST":
        errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return render(request, "srtv_shows_app/new_show.html")
    else:
        print(f'add show form info: {request.POST}')
        new_show = Show.objects.create(title=request.POST["title"],
        network=request.POST["network"],
        release_date=request.POST["release_date"],
        desc=request.POST["description"])
        messages.success(request, "Show successfully created")
    print(f'new show ID: {new_show.id}')
    return redirect(f'/shows/{new_show.id}')

def editShow(request, showID):
    show_data = {
        "show_info": Show.objects.get(id=showID)
    }
    return render(request, "srtv_shows_app/edit_show.html", show_data) 

def updateShow(request, showID):
    if request.method == "POST":
        errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        print(f'update information: {showID} {request.POST}')
        update_show = Show.objects.filter(id=showID).update(title=request.POST['title'],
        network=request.POST['network'], release_date=request.POST['release_date'],
        desc = request.POST['description'])
    return redirect(f'/shows/{showID}')

def destroyShow(request, showID):
    destroy = Show.objects.filter(id=showID).delete()
    print(f'deleted show ID: {showID}')
    return redirect(f'/shows')