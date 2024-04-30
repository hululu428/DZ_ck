from django.contrib import admin
from .models import BugReport, FeatureRequest

class BugReportInline(admin.TabularInline):
    model = BugReport
    extra = 0
    fields = ('status',)
    readonly_fields = ('title', 'project', 'created_at', 'updated_at')
    can_delete = True
    show_change_link = True

@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority') 
    list_filter = ('project', 'status', 'priority')
    search_fields = ('title', 'description')
    list_editable = ('status', 'priority')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority') 
    list_filter = ('project', 'status', 'priority')
    search_fields = ('title', 'description')
    list_editable = ('status', 'priority')
    readonly_fields = ('created_at', 'updated_at')


# Register your models here.
