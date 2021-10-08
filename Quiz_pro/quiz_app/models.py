from django.db import models
from django.contrib.auth.models import User

def upload_post_to(instance,filename):
	return f'post_picture/{instance.user.username}/{filename}'

class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	
class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	time = models.DateTimeField(auto_now_add=True)
	comm = models.TextField()

class SubComment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	time = models.DateTimeField(auto_now_add=True)
	comm = models.TextField()
	comment = models.ForeignKey(Comment, on_delete=models.CASCADE)