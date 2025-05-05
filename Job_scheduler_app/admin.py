from django.contrib import admin
from .models import Job, Applicant, InterviewSlot, Assignment

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'department', 'hiring_manager']
    search_fields = ['title', 'department']

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ['name', 'job', 'stage']
    list_filter = ['stage', 'job']
    search_fields = ['name']

@admin.register(InterviewSlot)
class InterviewSlotAdmin(admin.ModelAdmin):
    list_display = ['applicant', 'scheduled_time']
    list_filter = ['scheduled_time']

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['applicant', 'task_description', 'submitted']
    list_filter = ['submitted']
