from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from User.models import UserModel


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['username', 'name', 'role', 'last_login']
    search_fields = ['username', 'name', 'role', 'email']
    fieldsets = (
        (
            ("User Information"), {
                'fields': ('name', 'email', 'role', 'phone')
            }
        ),
        (
            ("Login Information"), {
                'fields': ('username', 'password')
            }
        ),
        (
            ("Permissions"), {
                'fields': ('is_active', 'is_staff', 'is_superuser')
            }
        ),
        (
            ("Important dates"), {
                'fields': ('last_login', 'date_joined')
            }
        ),
    )
    readonly_fields = ('last_login', 'date_joined')
    add_fieldsets = (
        (
            ("User Information"), {
                'classes': ('wide',),
                'fields': ('name', 'email', 'role', 'phone')
            }
        ),
        (
            ("Login Information"), {
                'classes': ('wide',),
                'fields': ('username', 'password1', 'password2')
            }
        )
    )

admin.site.register(UserModel, UserAdmin)