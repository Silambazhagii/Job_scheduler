from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    hiring_manager = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Applicant(models.Model):
    STAGES = [
        ('Applied', 'Applied'),
        ('Phone Screen', 'Phone Screen'),
        ('Interview', 'Interview'),
        ('Offer', 'Offer'),
        ('Hired', 'Hired'),
    ]
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    stage = models.CharField(max_length=20, choices=STAGES, default='Applied')

    def __str__(self):
        return self.name

class InterviewSlot(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    scheduled_time = models.DateTimeField()

    def __str__(self):
        return f"{self.applicant.name} - {self.scheduled_time}"

class Assignment(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    task_description = models.TextField()
    submitted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.applicant.name} - Submitted: {self.submitted}"
