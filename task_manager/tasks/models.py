from django.db import models
from django.utils import timezone

class Task(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Overdue', 'Overdue'),
        ('Completed', 'Completed'),
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def save(self, *args, **kwargs):
        # Automatically set status based on due_date
        if self.status != 'Completed':
            if self.due_date < timezone.now().date():
                self.status = 'Overdue'
            else:
                self.status = 'Pending'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
