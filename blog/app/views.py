from django.views import generic
from . import models

class PostsIndex(generic.ListView):
  queryset      = models.Post.objects.published()
  paginate_by   = 10