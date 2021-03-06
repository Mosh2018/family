from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'username', ]
    fieldsets = (
        (None, {'fields': ['username', 'email', 'password', ]}),
        ('Permissions',
         {'fields': ['is_active', 'is_staff', 'is_superuser', ]}
         ),
        ('Important dates', {'fields': ['last_login', ]})
    )

    add_fieldsets = (
        (None, {
            'classes': ['wide', ],
            'fields': ['username', 'email', 'password1', 'password2', ]
        }),
    )


admin.site.register(User, UserAdmin)
