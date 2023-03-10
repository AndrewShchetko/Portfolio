from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250, blank=True, default=None)
    date = models.DateField(default=None)

    def __str__(self):
        return self.title, self.description
