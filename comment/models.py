from django.db import models
from django.contrib.auth.models import User
from food.models import Article


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("created",)
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.body[:20]

