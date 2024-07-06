from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterFrom, VideoForm
from .models import Video


def register(request):
    if request.method == 'POST':
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterFrom()
    return render(request, 'testproject/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('video_list')
    else:
        form = AuthenticationForm()
        return render(request, 'testproject/login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('login')


def add_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.save()
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'testproject/add_video.html', {'form': form})


def video_list(request):
    videos = Video.objects.all()
    return render(request, 'testproject/video_list.html', {'videos': videos})


def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    return render(request, 'testproject/video_detail.html', {'video': video})
