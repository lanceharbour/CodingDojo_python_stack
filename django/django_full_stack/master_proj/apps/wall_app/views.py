from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Message, Comment
# Create your views here.
def viewWall(request):
    if 'userid' in request.session:
        context = {
            'user': User.objects.get(id = request.session['userid']),
            'all_posts': Message.objects.all()
        }
    else:
        return redirect(f'/')
    return render(request, "wall_app/thewall.html", context)

def newPost(request):
    if request.method == "POST":
            if 'userid' in request.session:
                Message.objects.create(message=request.POST["post"], 
                user=User.objects.get(id=request.session['userid']))
    return redirect(f'/wall')

def newComment(request):
    if request.method == "POST":
        if 'userid' in request.session:
            Comment.objects.create(comment=request.POST["comment"], 
            user=User.objects.get(id=request.session["userid"]), 
            message=Message.objects.get(id=request.POST["post_id"]))
    return redirect(f'/wall')

def delPost(request):
    if request.method == "POST":
        print("deleting post")
        deletepost = Message.objects.filter(id=request.POST["post_id"]).delete()
    return redirect(f'/wall')

def delComment(request):
    if request.method == "POST":
        print("deleting comment")
        deleletecom = Comment.objects.filter(id=request.POST["comment_id"]).delete()
    return redirect(f'/wall')
