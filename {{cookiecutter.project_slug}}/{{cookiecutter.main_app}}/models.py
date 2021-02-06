from django.db import models

class {{ cookiecutter.main_model }}(models.Model):
    description = models.CharField(max_length=264)
    due_to = models.DateTimeField()
    done = models.BooleanField(default=False)

    @property
    def status(self):
        return 'done' if self.done else 'pending'
