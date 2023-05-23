from django.db import models
from accounts.models import Account
from posts.models import Post
from django.shortcuts import reverse
from django.db.models.signals import pre_save
from main.utils import unique_slug_generator
from django.utils.text import slugify
from django.db.models import Q



class CommentQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            lookup = (Q(content__icontains=query))
            qs = qs.filter(lookup).distinct()
        return qs

class CommentManager(models.Manager):
    def get_queryset(self):
        return CommentQuerySet(self.model, using=self._db)
    def search(self, query=None):
        return self.get_queryset().search(query=query)

class Comment(models.Model):
	account   = models.ForeignKey(Account, on_delete=models.CASCADE)
	post      = models.ForeignKey(Post, on_delete=models.CASCADE)
	content   = models.TextField()
	slug      = models.SlugField(unique=True, blank=True)
	parent    = models.ForeignKey("self", null=True, blank=True, related_name='replies')
	is_active = models.BooleanField(default=True, blank=True)
	created   = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated   = models.DateTimeField(auto_now=True, auto_now_add=False)


	objects = CommentManager()

	def __str__(self):
		return str(self.account.user.first_name) + ' - ' + str(self.slug)

	@property
	def get_absolute_url(self):
		return reverse('comments:detail', kwargs={'slug': self.slug})

	@property
	def get_edit_url(self):
		return reverse('comments:edit', kwargs={'slug': self.slug})

	@property
	def get_delete_url(self):
		return reverse('comments:delete', kwargs={'slug': self.slug})

	class Meta:
		ordering = ['-created', 'is_active', ]


def pre_save_action(sender, instance, *args, **kwargs):
    content = instance.content
    if len(content) <= 40:
        slug = content
    else:
        slug = content[:40]
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, new_slug=slugify(slug))

pre_save.connect(pre_save_action, sender=Comment)