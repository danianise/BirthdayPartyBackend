from django.db import models

# Create your models here.

class Response(models.Model):
    name = models.CharField(max_length=100)
    adult_count = models.CharField(max_length=100, default=0)
    kids_count = models.CharField(max_length=100, default=0)
    message = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return '{}, {} adults and {} kids in party'.format(self.name, self.adult_count, self.kids_count)

class Decline(models.Model):
    name = models.CharField(max_length=100)
    decline_message = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return '{} has declined'.format(self.name)