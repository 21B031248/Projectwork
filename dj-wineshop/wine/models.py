from django.db import models

from taggit.managers import TaggableManager

class Wine(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True)
    quantity = models.IntegerField()
    tags = TaggableManager()
    details = models.TextField(null=True)

    def __str__(self):
        return self.name
