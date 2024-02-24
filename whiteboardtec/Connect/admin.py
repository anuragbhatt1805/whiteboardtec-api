from django.contrib import admin
from Connect.models import (
    Contact, Email, Address, Social, Connect
)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('primary', 'secondary')
    search_fields = ('primary', 'secondary')
    fieldsets = (
        (
            ("Primary Contact"), {
                'fields': ('primary',)
            }
        ),
        (
            ("Secondary Contact"), {
                'fields': ('secondary',)
            }
        ),
    )
    add_fieldsets = (
        (
            ("Contact Information"), {
                'classes': ('wide',),
                'fields': ('primary',)
            }
        )
    )

class EmailAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
    fieldsets = (
        (
            ("Email Information"), {
                'fields': ('name', 'email')
            }
        ),
    )
    add_fieldsets = (
        (
            ("Email Information"), {
                'classes': ('wide',),
                'fields': ('name', 'email')
            }
        )
    )

class AddressAdmin(admin.ModelAdmin):
    list_display = ('location',)
    search_fields = ('location', 'address_line1', 'address_line2', 'address_line3')
    fieldsets = (
        (
            ("Country"), {
                'fields': ('location',)
            }
        ),
        (
            ("Address"), {
                'fields': ('address_line1', 'address_line2', 'address_line3')
            }
        ),
    )
    add_fieldsets = (
        (
            ("Address Information"), {
                'classes': ('wide',),
                'fields': ('location', 'address_line1', 'address_line2', 'address_line3')
            }
        )
    )

class SocialAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')
    search_fields = ('name', 'link')
    fieldsets = (
        (
            ("Social Media"), {
                'fields': ('name', 'link')
            }
        ),
    )
    add_fieldsets = (
        (
            ("Social Media Information"), {
                'classes': ('wide',),
                'fields': ('name', 'link')
            }
        )
    )

class ConnectAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            ("Contact"), {
                'fields': ('contact',)
            }
        ),
        (
            ("Email"), {
                'fields': ('email',)
            }
        ),
        (
            ("Address"), {
                'fields': ('address',)
            }
        ),
        (
            ("Social Media"), {
                'fields': ('social',)
            }
        ),
    )
    add_fieldsets = (
        (
            ("Connect Information"), {
                'classes': ('wide',),
                'fields': ('contact', 'email', 'address', 'social')
            }
        )
    )

admin.site.register(Contact, ContactAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(Connect, ConnectAdmin)