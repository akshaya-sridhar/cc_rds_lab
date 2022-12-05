from django.db import models

# Create your models here.

class covid_19(models.Model):
    State_Name = models.CharField(max_length=100)
    Date_of_Record=models.DateField()
    No_of_Samples=models.IntegerField()
    No_of_Deaths=models.IntegerField()
    No_of_Positive=models.IntegerField()    
    No_of_Negative=models.IntegerField()
    No_of_Discharge=models.IntegerField()
    
    def __str__(self):
        return self.State_Name, self.No_of_Samples
