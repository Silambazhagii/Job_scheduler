from django.shortcuts import render, redirect
from .forms import InterviewSlotForm

def create_interview(request):
    if request.method == 'POST':
        form = InterviewSlotForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., save it to the database)
            # You can store it in a model if you wish to save it for future use
            # Example:
            # InterviewSlot.objects.create(
            #     candidate_name=form.cleaned_data['candidate_name'],
            #     job_role=form.cleaned_data['job_role'],
            #     interview_date=form.cleaned_data['interview_date'],
            #     interview_time=form.cleaned_data['interview_time'],
            #     notes=form.cleaned_data.get('notes')
            # )
            return redirect('create_interview')  # Redirect after POST to avoid re-submission on refresh
    else:
        form = InterviewSlotForm()

    return render(request, 'create_interview.html', {'form': form})
