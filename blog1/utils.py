import json

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import Post


class BlogUtils:

    @staticmethod
    def load_posts():
        with open('post.json') as f:
            data = json.load(f)
        for x in data:
            posts = Post.objects.create(title=x['title'], content=x['content'],
                                        author=get_object_or_404(User, id=x['user_id']))
            posts.save()
