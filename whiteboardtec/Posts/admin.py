from django.contrib import admin
from Posts.models import Post


class PostAdmin(admin.ModelAdmin):
    ordering = ('-created_at',)
    list_display = ('title', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('title', 'content',)
    fieldsets = (
        (
            ("Post Information"), {
                'fields': ('title', 'content', 'image', 'link')
            }
        ),
        (
            ("Status"), {
                'fields': ('is_active',)
            }
        ),
        (
            ("Important dates"), {
                'fields': ('created_at', 'updated_at')
            }
        ),
    )
    readonly_fields = ('created_at', 'updated_at')
    add_fieldsets = (
        (
            ("Post Information"), {
                'classes': ('wide',),
                'fields': ('title', 'content',)
            }
        )
    )

admin.site.register(Post, PostAdmin)