from django import forms
from .models import InterviewSlot

class InterviewSlotForm(forms.Form):
    candidate_name = forms.CharField(label='Candidate Name', max_length=100)
    job_role = forms.CharField(label='Job Role', max_length=100)
    interview_date = forms.DateField(label='Interview Date', widget=forms.DateInput(attrs={'type': 'date'}))
    interview_time = forms.TimeField(label='Interview Time', widget=forms.TimeInput(attrs={'type': 'time'}))
    notes = forms.CharField(label='Additional Notes', widget=forms.Textarea, required=False)
