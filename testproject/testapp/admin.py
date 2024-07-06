from django.contrib import admin

from .models import Video, Comment, User
from django.contrib.auth.admin import UserAdmin
from .forms import UserRegisterFrom


class RegUserAdmin(UserAdmin):
    add_form = UserRegisterFrom
    model = User
    list_display = ['user', 'user_name', 'phone_number', 'is_active', 'is_staff', 'is_superuser']
    fieldsets = (
        (None, {'fields': ('username', 'password2')}),
        ('Personal info', {'fields': ('user_name', 'phone_number',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',)})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields ': ('username', 'user_name', 'phone_number', 'password2', 'is_active', 'is_staff', 'is_superuser')}
         ),
    )


admin.site.register(User, UserAdmin)
admin.site.register(Video)
admin.site.register(Comment)
