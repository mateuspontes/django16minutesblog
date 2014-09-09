from django.db import models

class PostQuerySet(models.QuerySet):
  def published(self):
    return self.filter(publish = True)

class Post(models.Model):
  title      = models.CharField(max_length = 200)
  text       = models.TextField()
  slug       = models.SlugField(max_length = 200, unique = True)
  publish    = models.BooleanField(default = True)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)

  objects = PostQuerySet.as_manager()

  def __str__(self):
    return self.title

  class Meta:
    verbose_name_plural = "Posts do Blog"
    ordering = ["-created_at"]