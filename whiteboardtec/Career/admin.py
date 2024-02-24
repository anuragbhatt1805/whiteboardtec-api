from django.contrib import admin
from Career.models import (
    Job, Application,
)

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    "Admin for Job"
    list_display = (
        'title', 'location', 'type', 'is_active',
    )
    search_fields = (
        'title', 'location', 'type', 'created_at',
    )
    list_filter = (
        'location', 'type', 'qualification', 'is_active', 'created_at', 'updated_at'
    )
    fieldsets = (
        (
            None, {
                'fields': (
                    'id',
                )
            }
        ),
        (
            ('Job Details'), {
                'fields': (
                    'title', 'description', 'location', 'type', 'qualification',
                )
            }
        ),
        (
            ('Job Files'), {
                'fields': (
                    'job_description',
                )
            }
        ),
        (
            ('Status'), {
                'fields': (
                    'is_active',
                )
            }
        ),
        (
            ('Timestamps'), {
                'fields': (
                    'created_at', 'updated_at',
                )
            }
        ),
    )
    readonly_fields = (
        'id', 'created_at', 'updated_at',
    )
    add_fieldsets = (
        (
            ('Job Details'), {
                'fields': (
                    'title', 'location', 'type', 'qualification',
                )
            }
        ),
        (
            ('Job Files'), {
                'fields': (
                    'job_description',
                )
            }
        )
    )

class ApplicationAdmin(admin.ModelAdmin):
    "Admin for Application"
    list_display = (
        'job', 'name', 'email', 'created_at',
    )
    search_fields = (
        'job', 'name', 'email', 'phone',
    )
    list_filter = (
        'job', 'created_at',
    )
    fieldsets = (
        (
            None, {
                'fields': (
                    'id',
                )
            }
        ),
        (
            ('Job Details'), {
                'fields': (
                    'job',
                )
            }
        ),
        (
            ('Applicant Details'), {
                'fields': (
                    'name', 'email', 'phone',
                )
            }
        ),
        (
            ('Documents'), {
                'fields': (
                    'resume',
                )
            }
        ),
        (
            ('Additional Information'), {
                'fields': (
                    'cover_letter',
                )
            }
        ),
        (
            ('Timestamps'), {
                'fields': (
                    'created_at',
                )
            }
        ),
    )
    readonly_fields = (
        'id', 'created_at',
    )
    add_fieldsets = (
        (
            ('Select Job'), {
                'fields': (
                    'job',
                )
            }
        ),
        (
            ('Applicant Details'), {
                'fields': (
                    'name', 'email', 'phone',
                )
            }
        ),
        (
            ('Resume'), {
                'fields': (
                    'resume',
                )
            }
        ),
        (
            ('Additional Information'), {
                'fields': (
                    'cover_letter',
                )
            }
        ),
    )


admin.site.register(Job, JobAdmin)
admin.site.register(Application, ApplicationAdmin)