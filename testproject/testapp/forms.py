from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Video


class UserRegisterFrom(UserCreationForm):
    user_name = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['username', 'user_name', 'phone_number', 'password2']


class UserChangeInfoForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'user_name', 'phone_number', 'password2']


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['video_title', 'video_content']
