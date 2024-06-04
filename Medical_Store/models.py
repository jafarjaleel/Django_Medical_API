from django.db import models

class Medicine(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0.0)


    def __str__(self):
        return self.name

