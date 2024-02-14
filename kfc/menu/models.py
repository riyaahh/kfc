from django.db import models
from django.contrib.auth.models import User

class userdetails(models.Model):
    user=models.OneToOneField(User,primary_key='True',on_delete=models.CASCADE)
    phoneno=models.IntegerField()
    emailid=models.CharField(max_length=20)
    gender= models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],default='DefaultGender')
    

    def __str__(self):

        return str(self.user.__str__())


