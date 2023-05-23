from django.db import models
from accounts.models import Account
from posts.models import Post

class Like(models.Model):
	account = models.ForeignKey(Account, on_delete=models.CASCADE)
	post    = models.ForeignKey(Post, on_delete=models.CASCADE)
