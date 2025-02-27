from django.db import models
from datetime import date

class Management(models.Model):
    id = models.AutoField(primary_key=True)  
    title = models.CharField(max_length=100)  
    description = models.TextField(blank=True, null=True)  
    due_date = models.DateField()  
    status = models.CharField(max_length=20, default="Not Yet Started") 
    
    def __str__(self):  
        return self.title
