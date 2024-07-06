from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_name = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    password2 = models.CharField(max_length=128)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='werfthegagth',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permissions',
        related_name='customuser_set',
        blank=True,
        help_text='wedfrgbhte',
        verbose_name='user_permissions',
    )

    def __str__(self):
        return self.username


class Video(models.Model):
    video_title = models.CharField(max_length=255)
    video_content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.video_title


class Comment(models.Model):
    comment_text = models.TextField()
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text
