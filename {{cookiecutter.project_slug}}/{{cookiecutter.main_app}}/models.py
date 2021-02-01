from django.db import models

class {{ cookiecutter.main_model }}(models.Model):
    description = models.CharField(max_length=264)
    due_to = models.DateTimeField()

