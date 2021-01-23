from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=256)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
