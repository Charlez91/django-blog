from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    content = RichTextField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> reverse:
        return reverse('post-detail', kwargs={'pk': self.pk})
