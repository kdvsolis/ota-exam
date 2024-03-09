from django.db import models

class Email(models.Model):
    content = models.TextField()
    is_newsletter = models.BooleanField()