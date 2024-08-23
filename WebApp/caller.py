import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WebApp.settings")
django.setup()

from django.contrib.auth.models import User
from WebApp.blog.models import Post
import random


def create_post():
    for i in range(7, 28):
        post = Post()
        post.title = f'Blog {i}'
        post.content = f'Post Content {i} is created'
        id_ = random.choice([1, 2, 9, 10, 11])

        current_author = User.objects.get(pk=id_)

        post.author = current_author
        post.save()
    print("Done")

create_post()

# 1 ,2 6, 7, 8, 9,
