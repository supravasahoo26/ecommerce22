from django.db import models
#from productapp import models


class Signup(models.Model):
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    username=models.CharField(primary_key=True,max_length=10)
    phone_no=models.IntegerField()
    email= models.EmailField(max_length=50)
    password= models.CharField(max_length=20)
    rpsw= models.CharField(max_length=20)
    def get_fname(self):
        return self.firstname
    #def get_lastname(self):
       # return self.lastname
    #def get_username(self):
        #return self.username
    #def get_phone_no(self):
        #return self.phone_no
    #def get_email(self):
        #return self.email
   # def get_password(self):
        #return self.password
    #def get_rpsw(self):
        #return self.rpsw


class Signin(models.Model):
    username = models.CharField(primary_key=True,max_length=10)
    password= models.CharField(max_length=20)
    def get_user(self):
        return self.username
    def get_pswd(self):
        return self.password










