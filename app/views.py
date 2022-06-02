import re
from django.shortcuts import render, redirect
from .models import Posts
from .forms import PostCreate
from django.http import HttpResponse
def index(request):
    posts=Posts.objects.all()
    return render(request,'posts.html',{'posts':posts})
def upload(request):
    upload=PostCreate()
    if request.method=='POST':
        upload=PostCreate(request.POST,request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("Your form is wrong")

    else:
        return render(request,'upload_form.html',{'upload_form':upload})
def update_post(request,post_id):
    post_id=int(post_id)
    try:
        post_up=Posts.objects.get(id=post_id)
    except Posts.DoesNotExist:
        return redirect('index' )
    post_form=PostCreate(request.POST or None,instance=post_up)
    if post_form.is_valid():
        post_form.save()
        return redirect('index')
    return render(request,'upload_form.html',{'upload_form':post_form})
def delete_post(request,post_id):
    post_id=int(post_id)
    try:
        post_up=Posts.objects.get(id=post_id)
    except Posts.DoesNotExist:
        return redirect('index')
    post_up.delete()
    return redirect('index')


    




# Create your views here.
