from django.contrib import admin
from Portfolio.models import Image, Portfolio


class ImageAdmin(admin.ModelAdmin):
    list_display = ['caption', 'image',]
    search_fields = ['caption', 'image', 'created_at']
    list_filter = ['caption', 'created_at']
    fieldsets = (
        (
            'Image', {
                'fields': ('caption', 'image')
            }
        ),
        (
            'Dates', {
                'fields': ('created_at',)
            }
        ),
    )
    add_fieldsets = (
        (
            'Image', {
                'fields': ('image',)
            }
        ),
    )

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated_at']
    search_fields = ['title', 'description',]
    list_filter = ['title', 'created_at', 'updated_at']
    fieldsets = (
        (
            'Portfolio', {
                'fields': ('title', 'description',)
            }
        ),
        (
            'Documents', {
                'fields': ('image', 'document',)
            }
        ),
        (
            'Dates', {
                'fields': ('created_at', 'updated_at')
            }
        ),
    )
    add_fieldsets = (
        (
            'Portfolio', {
                'fields': ('title', 'description', 'image', 'document')
            }
        ),
    )

admin.site.register(Image, ImageAdmin)
admin.site.register(Portfolio, PortfolioAdmin)