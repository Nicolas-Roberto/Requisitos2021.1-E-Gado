from django.db import models
# Create your models here.

class RationFarm(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, blank=False, max_length=200)
    preco = models.FloatField(null=False, blank=False)
    quantidade = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return str(self.name)