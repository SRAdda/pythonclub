from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class clubType(models.Model):
    typename = models.CharField(max_length=255)
    typedescription=models.CharField(max_length=255)

    def __str__(self): 
        return self.typename
        class Meta:
            db_table='clubtype'


class clubProduct(models.Model):
    productname=models.CharField(max_length=255)
    clubtype=models.ForeignKey(clubType, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    entryDate=models.DateField()
    productURL=models.URLField()
    productdescription=models.TextField()

    def __str__(self):
        return self.productname
        
    class Meta:
        db_table='clubproduct'