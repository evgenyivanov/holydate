from django.db import models

class Users_trace(models.Model):
    date = models.DateTimeField()
    ip = models.CharField(max_length=30)