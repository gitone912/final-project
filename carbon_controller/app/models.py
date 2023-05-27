from django.db import models

class EmissionFactor(models.Model):
    name = models.CharField(max_length=100)
    factor = models.FloatField()

    def __str__(self):
        return self.name
