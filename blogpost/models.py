from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class Blog(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=300,blank=True,null=True)
    image=models.ImageField(upload_to="postimg/")
    blogs=models.TextField(blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    comment=models.ManyToManyField('Comment')
    like=models.ManyToManyField('Like')

    def __str__(self):
        return self.user.username


class Contact(models.Model):
    name=models.CharField(max_length=300,blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    subject=models.CharField(max_length=400,blank=True,null=True)
    description=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    comment_user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField(blank=True,null=True)
    comment_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    comment_likes=models.ManyToManyField("C_Like",blank=True,null=True)

    def __str__(self):
        return str(self.comment_user)

class Like(models.Model):
    liked_user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.liked_user.username

class C_Like(models.Model):
    C_liked_user=models.ForeignKey(User,on_delete=models.CASCADE)

class About(models.Model):
    title=models.CharField(max_length=300,blank=True,null=True)
    image=models.ImageField(upload_to="postimg/")
    post=models.TextField(blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.title