from django.db import models

# Create your models here.

class data_application(models.Model): 
    first_name=models.CharField( max_length=255)
    last_name=models.CharField( max_length=255)
    phone=models.IntegerField(null=True)
    Date=models.DateField(null=True)
    
    
    
    