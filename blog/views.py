from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Like, Profile
from django.contrib import messages

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        if request.user.is_authenticated:
            Comment.objects.create(
                post=post,
                user=request.user,
                content=request.POST.get('content')
            )
        return redirect('post_detail', id=id)

    return render(request, 'post_detail.html', {'post': post})


@login_required
def create_post(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')

        if not title or not content:
            return render(request, 'create_post.html', {
                'error': 'Title and Content are required!'
            })

        Post.objects.create(
            title=title,
            content=content,
            image=image,
            author=request.user
        )

        return redirect('home')

    return render(request, 'create_post.html')


@login_required
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.user != post.author:
        return redirect('home')

    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')

        if request.FILES.get('image'):
            post.image = request.FILES.get('image')

        post.save()
        return redirect('post_detail', id=post.id)

    return render(request, 'edit_post.html', {'post': post})


@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.user == post.author:
        post.delete()

    return redirect('home')


@login_required
def like_post(request, id):
    post = get_object_or_404(Post, id=id)

    like, created = Like.objects.get_or_create(
        post=post,
        user=request.user
    )

    if not created:
        like.delete()

    return redirect(request.META.get('HTTP_REFERER', 'home'))


User = get_user_model()

def register(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('register')

        first_name = full_name.split()[0]
        last_name = " ".join(full_name.split()[1:])

        username = email.split("@")[0]

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        return redirect('login')

    return render(request, 'register.html')


def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Invalid email or password.")
            return redirect('login')

        user = authenticate(username=user_obj.username, password=password)

        if user is None:
            messages.error(request, "Invalid email or password.")
            return redirect('login')

        # If admin → redirect to admin panel
        if user.is_staff or user.is_superuser:
            login(request, user)
            return redirect('/admin/')

        login(request, user)
        return redirect('home')

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        profile.bio = request.POST.get('bio')

        if request.FILES.get('image'):
            profile.image = request.FILES.get('image')

        profile.save()
        return redirect('profile')

    return render(request, 'edit_profile.html', {'profile': profile})

@login_required
def profile(request):
    if request.user.is_staff or request.user.is_superuser:
        return redirect('/admin/')

    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'profile.html', {'profile': profile})