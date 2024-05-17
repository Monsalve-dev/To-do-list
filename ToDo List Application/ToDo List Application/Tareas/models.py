from django.db import models


# Create your models here.

class Adminis(models.Model):
    Title = models.CharField(primary_key=True, max_length=50)
    Descrip = models.CharField(max_length=200)
    Checked = models.BooleanField
    
    def __str__(self) -> str:
        text= "{0} ({1})"
        return text.format(self.Title, self.Descrip)