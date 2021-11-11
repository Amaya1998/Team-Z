from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from .forms import PostForm
from django.contrib.auth.models import User

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def Register(request):

    if request.method == "POST":
        user = User.objects.create_user(request.POST.get('username'), request.POST.get('email'), request.POST.get('password'))

        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.is_staff = 1

        user.save()
        return redirect('posts')
    return render(request, 'post/register.html')

def ViewPost(request):

    posts = Post.objects.all()
    comments = Comment.objects.all()
    users = User.objects.all()

    if request.method == "POST":

        comment = Comment()
        comment.Comment = request.POST.get('comment')
        comment.Create_by = request.user.username
        comment.Post_ID_id = request.POST.get('post')
        comment.save()
        # messsages.success(request, "Product Added Successfully")
        return redirect('posts')

    return render(request, 'post/index.html', {'post': posts, 'comment': comments, 'users': users})

def CreatePost(request):

    # form = PostForm()

    if request.method == "POST":

        post = Post()
        post.User_ID_id = request.user.id
        post.Title = request.POST.get('title')
        post.Description = request.POST.get('description')
        post.Create_by = request.user.username

        if len(request.FILES) != 0:
            post.Image = request.FILES['image']

        post.save()
        # messsages.success(request, "Product Added Successfully")
        return redirect('posts')

        # print(request.POST)
        # form = PostForm(request.POST)
        # if form.is_valid():
        #     form.save()

    # content = {'form': form}
    return render(request, 'post/form.html')

    
