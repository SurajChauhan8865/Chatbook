from django.db import models


class AccountUser(models.Model):
    uid=models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=20)
    surname=models.CharField(max_length=20)
    username=models.CharField(max_length=50)
    email=models.EmailField(default=None,blank=True,null=True)
    gender=models.CharField(max_length=20)
    dob=models.DateField()
    img=models.ImageField(upload_to='images',default=None,blank=True,null=True)
    work=models.CharField(max_length=500,default=None,blank=True,null=True)
    qualification=models.CharField(max_length=200,default=None,blank=True,null=True)
    currenttown=models.CharField(max_length=50,default=None,blank=True,null=True)
    hometown=models.CharField(max_length=50,default=None,blank=True,null=True)
    friend=models.IntegerField(default=0,blank=True,null=True)
    relationship=models.CharField(max_length=50,default=None,blank=True,null=True)
    otp=models.IntegerField(default=0,blank=True,null=True)


    def __str__(self):
        return self.firstname+' '+self.surname+' '+self.username