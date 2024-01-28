from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    estimated_end_date = models.DateField()
    percentage_completed = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    
    def update_percentage_completed(self):
        total_tasks = self.task_set.count()
        completed_tasks = self.task_set.filter(status='Done').count()
        
        if total_tasks == 0:
            self.percentage_completed = 0
        else:
            self.percentage_completed = (completed_tasks / total_tasks) * 100

        self.save()

class Task(models.Model):
    STATUS_CHOICES = (
        ('Todo', 'Todo'),
        ('In Progress', 'In Progress'),
        ('Review', 'Review'),
        ('Done', 'Done'),
    )

    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Todo')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
