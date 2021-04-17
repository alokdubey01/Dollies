from django.db import models

class Books(models.Model):
  book_id=models.AutoField
  book_name=models.CharField(max_length=255)
  category=models.CharField(max_length=255)
  desc=models.CharField(max_length=255)
  image=models.ImageField()
  document=models.FileField()
  
  def __str__(self):
    return self.book_name
    
    
class Contact(models.Model):
     sno= models.AutoField
     name= models.CharField(max_length=255)
     #phone= models.CharField(max_length=13)
     email= models.CharField(max_length=100)
     content= models.TextField()
     
def __str__(self):
 return 'massage from - '+self.name