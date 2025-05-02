from django.contrib import admin
from .models import Job, Applicant, InterviewSlot, Assignment

admin.site.register(Job)
admin.site.register(Applicant)
admin.site.register(InterviewSlot)
admin.site.register(Assignment)
