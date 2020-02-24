from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=500)
    slug = models.CharField(max_length=70, null="True")

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug':self.slug})

    def __str__(self):
        return self.title

class Comment(models.Model):
    body = models.CharField(max_length=200)
    post = models.ForeignKey(Post, blank="True", null="True", on_delete=models.CASCADE)

    def __str__(self):
        return self.body

class Tag(models.Model):
    name = models.CharField(max_length=20)
    posts = models.ManyToManyField(Post)

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'name':self.name})

    def __str__(self):
        return self.name