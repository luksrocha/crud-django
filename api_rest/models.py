from django.db import models

# Create your models here.
class User(models.Model):
    user_nickname = models.CharField(max_length=100, primary_key=True, default="")
    user_name = models.CharField(max_length=150, default="")
    user_email = models.CharField(max_length=200, default="")
    user_age = models.IntegerField(default=0)

    def __str__(self):
        return f'Nickname: {self.user_name} | E-mail: {self.user_email}'
    
class UserTasks (models.Model):
    user_nickname = models.CharField(max_length=100, default="")
    user_task = models.CharField(max_length=255, default="")