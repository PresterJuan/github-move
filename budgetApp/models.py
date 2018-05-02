from django.db import models

# Create your models here.
class Stuff(models.Model):
    top_name = models.CharField(max_length=264,unique=True)
    budgeted = models.FloatField()
    actual = models.FloatField()

    def __str__(self):
        x = self.top_name + ": Budgeted - " + str(self.budgeted) + ", Actual -  " + str(self.actual)
        return x
