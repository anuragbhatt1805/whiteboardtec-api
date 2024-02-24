from django.contrib import admin
from Gallery.models import Gallery


class GalleryAdmin(admin.ModelAdmin):
    ordering = ('-created_at',)
    list_display = ('caption', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'created_at')
    fieldsets = (
        (
            ("Image Information"), {
                'fields': ('caption', 'image',)
            }
        ),
        (
            ("Important dates"), {
                'fields': ('created_at',)
            }
        ),
    )
    readonly_fields = ('created_at',)
    add_fieldsets = (
        (
            ("Post Information"), {
                'classes': ('wide',),
                'fields': ('image',)
            }
        )
    )

admin.site.register(Gallery, GalleryAdmin)