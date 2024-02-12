from django.db import models

class Trade(models.Model):
    date = models.DateField()
    trade_code = models.CharField(max_length=20)
    high = models.FloatField()
    low = models.FloatField()
    open = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()
    
    
class DatabaseModel(models.Model):
    date = models.DateField()
    trade_code = models.CharField(max_length=20)
    high = models.FloatField()
    low = models.FloatField()
    open = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()
    
 
   
