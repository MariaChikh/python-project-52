from django.db import models
from task_manager.statuses.models import Status
from django.contrib.auth.models import User

class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_created')
    executor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks_assigned')
    #labels = models.ManyToManyField('Label')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
