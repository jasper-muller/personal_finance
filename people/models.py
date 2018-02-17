from django.db import models

# Create your models here.

class People(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name + ', age ' + str(self.age)
