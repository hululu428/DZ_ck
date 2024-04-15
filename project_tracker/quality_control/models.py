from django.db import models
from tasks.models import Project, Task

class BugReport(models.Model):
    STATUS_CHOICES = [
        ('New', 'Новая'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершена'),
    ]  

    title = models.CharField(max_length=50)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name = 'bugReport',
        on_delete = models.CASCADE    
    )
    task = models.ForeignKey(
        Task,
        related_name = 'bugReport',
        on_delete = models.SET_NULL,
        null = True,
        blank = True
    )
    status = models.CharField(
        max_length = 50,
        choices = STATUS_CHOICES,
        default = 'New'
    )
    priority = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class FeatureRequest(models.Model):
    STATUS_CHOICES = [
        ('New', 'Рассмотрение'),
        ('In_progress', 'Принято'),
        ('Completed', 'Отклонено'),
    ]  
    title = models.CharField(max_length=50)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name = 'featureRequest',
        on_delete = models.CASCADE    
    )
    task = models.ForeignKey(
        Task,
        related_name = 'featureRequest',
        on_delete = models.SET_NULL,
        null = True,
        blank = True
    )
    status = models.CharField(
        max_length = 50,
        choices = STATUS_CHOICES,
        default = 'New'
    )
    priority = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


