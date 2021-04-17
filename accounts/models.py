from django.db import models

# Create your models here.
class Contact(models.Model):
  contact_id = models.AutoField
  name =  models.CharField(max_length=50)
  email = models.EmailField(max_length=120)
  subject = models.CharField(max_length=500)
  
def __str__(self):
        return self.name