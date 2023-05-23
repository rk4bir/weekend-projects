from django.db import models
from accounts.models import Account
from posts.models import Post
from django.shortcuts import reverse


class Notification(models.Model):
	account = models.ForeignKey(Account, on_delete=models.CASCADE)
	post    = models.ForeignKey(Post, on_delete=models.CASCADE)
	content = models.TextField()
	is_seen = models.BooleanField(default=False, blank=True)
	created = models.DateTimeField(auto_now=False, auto_now_add=True)

	def get_seen_status_link(self):
		return reverse('notf-seen', kwargs={'pk': self.pk})

	
	class Meta:
		ordering = ['-created']

	def __str__(self):
		return str(self.account.user.username) + " - " + str(self.content) 