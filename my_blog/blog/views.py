from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post  # Assuming you have a Post model
from .forms import PostForm, LoginForm  # Assuming you have forms for Post and Login

def home_view(request):
    # Redirect to post_list if the user is already logged in
    if request.user.is_authenticated:
        return redirect('post_list')
    return render(request, 'blog/login.html')  # Render login page from blog directory

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)  # Assume you have a LoginForm defined
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('post_list')  # Redirect to post list after login
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'blog/login.html', {'form': form})  # Render login page

@login_required  # Ensure user is logged in to view posts
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})  # Render post list from blog directory

@login_required  # Ensure user is logged in to create a post
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post created successfully!')
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})  # Render post creation page from blog directory

@login_required  # Ensure user is logged in to view post details
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})  # Render post detail page from blog directory

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')  # Redirect to home (login page) after logout
