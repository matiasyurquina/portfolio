from django.db import models

class contact_model(models.Model):
    name = models.CharField(max_length=128, null=False)
    mail = models.CharField(max_length=128, null=False)
    subject = models.CharField(max_length=128, null=False)
    message = models.TextField(null=False)