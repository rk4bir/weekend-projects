from django.db import models
from accounts.models import Account
from django.shortcuts import reverse
from django.db.models.signals import pre_save
from main.utils import unique_slug_generator
from django.utils.text import slugify
from django.db.models import Q




class PostQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            lookup = (Q(content__icontains=query))
            qs = qs.filter(lookup).distinct()
        return qs

class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)
    
    






class Post(models.Model):
    account  = models.ForeignKey(Account, on_delete=models.CASCADE)
    slug     = models.SlugField(unique=True, blank=True, null=True)
    content  = models.TextField()
    photo1   = models.ImageField(upload_to="posts/",
                      null=True,
                      blank=True,
                      width_field="width_field1",
                      height_field="height_field1",
                    )
    drive_photo1_link = models.CharField(max_length=1000, default='', blank=True, null=True)
    height_field1 = models.IntegerField(default=0)
    width_field1 = models.IntegerField(default=0)

    photo2   = models.ImageField(upload_to="posts",
                      null=True,
                      blank=True,
                      width_field="width_field2",
                      height_field="height_field2",
                    )
    drive_photo2_link = models.CharField(max_length=1000, default='', blank=True, null=True)
    height_field2 = models.IntegerField(default=0)
    width_field2 = models.IntegerField(default=0)

    photo3   = models.ImageField(upload_to="posts",
                      null=True,
                      blank=True,
                      width_field="width_field3",
                      height_field="height_field3",
                    )
    drive_photo3_link = models.CharField(max_length=1000, default='', blank=True, null=True)
    height_field3 = models.IntegerField(default=0)
    width_field3 = models.IntegerField(default=0)
    likes = models.PositiveIntegerField(default=0, blank=True)
    comments = models.PositiveIntegerField(default=0, blank=True)
    is_active  = models.BooleanField(default=True, blank=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)



    objects = PostManager()


    def __str__(self):
        return str(self.account.user.first_name) + ' - ' + str(self.slug)

    @property
    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'slug': self.slug})

    @property
    def get_edit_url(self):
        return reverse('posts:edit', kwargs={'slug': self.slug})
    
    @property
    def get_delete_url(self):
        return reverse('posts:delete', kwargs={'slug': self.slug})
    class Meta:
        ordering = ['-created']

def pre_save_action(sender, instance, *args, **kwargs):
    content = instance.content
    if len(content) <= 40:
        slug = content
    else:
        slug = content[:40]
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, new_slug=slugify(slug))

pre_save.connect(pre_save_action, sender=Post)