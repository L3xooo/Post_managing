from django.shortcuts import render, redirect
from .models import Post
from .forms import PostEdit, PostForm
import requests


def home(request):
    if 'q' in  request.GET:
        id1 = int(request.GET['q'])
        posts = Post.objects.filter(id = id1)
        if bool(posts) == False:
            url = f'https://jsonplaceholder.typicode.com/posts/{id1}'
            response = requests.get(url)
            data = response.json()
            if bool(data) != False:
                post = Post(
                    id = data['id'],
                    userId = data['userId'],
                    title = data['title'],
                    body = data['body']
                )
                post.save()
                posts = Post.objects.filter(id = id1)
            else:
                return redirect('home')

    elif 'k' in request.GET:
        id1 = int(request.GET['k'])
        posts = Post.objects.filter(userId = id1)
    else:
        posts = Post.objects.all()
    return render(request,'base/home.html',{'posts':posts})

        
def createView(request):
    if request.method == "POST":
        form = PostForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request,'base/create.html',{'form':form})
        

def deleteView(request,pk):
    post = Post.objects.get(id = pk)
    if request.method == "POST":
        post.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'obj': post})

def editView(request,pk):
    post = Post.objects.get(id = pk)
    form = PostEdit(instance = post)

    if request.method == "POST":
        form = PostEdit(request.POST,instance=post)
        if form.is_valid():
            post.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'base/edit.html',context)
