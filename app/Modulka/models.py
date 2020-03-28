from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime


from pytils.translit import slugify


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(post_status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    #ID = models.IntegerField(primary_key=True)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Modulka_posts', default=0)
    post_content = models.TextField()
    post_title = models.CharField(max_length=200)
    #post_name = models.CharField(max_length=20, default='open')
    post_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    post_type = models.CharField(max_length=20,default='Post')
    publish = models.DateTimeField(default=timezone.now)
    post_modified = models.DateTimeField(auto_now=True)

    slug = models.SlugField(max_length=250,
                            unique=True)
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.post_title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.post_title)
        return super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('Modulka:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug
                             ])



class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)