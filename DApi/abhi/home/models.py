from django.db import models
class Emp(models.Model):
    ename=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.ename    

# Create your models here.
