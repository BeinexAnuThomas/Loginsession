from django.db import models
from django.core.validators import MinLengthValidator
from LoginSessionapp.validators import age_validation

# Create your models here.

choice=[('---','---'),('Male','Male'),('Female','Female')]

class Login(models.Model):
    email = models.EmailField(max_length=100,blank=False,null=True)
    full_name=models.CharField(max_length=50,blank=False,null=True)
    gender =models.CharField(max_length=40,choices = choice,default='---')
    age = models.IntegerField(validators=[age_validation])

    def __str__(self):
        return self.full_name

   