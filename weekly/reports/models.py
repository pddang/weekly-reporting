from django.db import models


class Report(models.Model):
    name = models.CharField("Full name", max_length=255)
    department = models.CharField("Department", max_length=255)
    activitiesCompleted = models.TextField("Activities Completed", null=False)
    activitiesInProgress = models.TextField("Activities In Progress", null=True)
    activitiesNextWeek = models.TextField("Activities Next Week", null=True)
    issues = models.TextField("Any Issues?", null=True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)
    

    def __str__(self):
        return self.name