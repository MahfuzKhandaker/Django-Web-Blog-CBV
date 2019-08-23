from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post-by-category', args=[self.pk])


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    view_count = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[self.pk])


class Comment(models.Model):
    comment_by = models.CharField(max_length=60)
    comment_body = models.TextField()
    comment_created_on = models.DateTimeField(auto_now_add=True)
    post =models.ForeignKey(Post, on_delete=models.CASCADE)