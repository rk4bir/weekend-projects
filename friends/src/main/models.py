from django.db import models


class Contact(models.Model):
	name    = models.CharField(max_length=100, blank=False, null=False)
	email   = models.CharField(max_length=200, blank=False, null=False)
	subject = models.CharField(max_length=500, blank=False, null=False)
	message = models.TextField()

	def __str__(self):
		return self.email + ' - ' + self.message