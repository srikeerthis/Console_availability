from django.db import models

# Create your models here.
class Console(models.Model):
    name = models.CharField(max_length=100)
    is_rented = models.BooleanField(default=False)

    def __str__(self):
        return self.name
