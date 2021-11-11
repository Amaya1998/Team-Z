from django.db import models
from django.contrib.auth.models import User
    

class Post(models.Model):
    User_ID = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    ID= models.BigAutoField(primary_key=True)
    Image= models.ImageField()
    Title= models.CharField(max_length=512, default='No Caption')
    Description= models.CharField(max_length=512)
    Create_by=models.CharField(max_length=512, default='MBAdmin')
    Create_at= models.DateField(auto_now_add=True)

def __str__(self):
    return '%s - %s' %(self.Image, self.Description)

class Comment(models.Model):
    Post_ID=models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    ID=models.BigAutoField(primary_key=True)
    Comment=models.CharField(max_length=512)
    Create_by=models.CharField(max_length=512)
    Create_at=models.DateField(auto_now_add=True)
    # @property
    # def user(self):
    #     return User.objects.get(pk=self.Create_by)

def __str__(self):
    return '%s - %s' %(self.post.Description, self.post.Create_at)

   