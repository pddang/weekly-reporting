from django.db import models


class Account(models.Model):
    firstName = models.CharField("First name", max_length=255)
    lastName = models.CharField("Last name", max_length=255)
    email = models.EmailField()
    username = models.CharField("Username", max_length=255)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)
    

    def __str__(self):
        return self.firstName