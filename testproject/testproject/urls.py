
from django.contrib import admin
from django.urls import path

from testapp.views import add_video, video_detail, video_list, logout, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('add_video/', add_video, name='add_video'),
    path('', video_list, name='video_list'),
    path('video/<int:pk>/', video_detail, name='video_detail'),
]
