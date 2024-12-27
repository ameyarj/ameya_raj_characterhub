from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.demo.models import Post, Comment
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Populates the database with test data'

    def handle(self, *args, **kwargs):
        users = []
        for i in range(5):
            user = User.objects.create_user(
                username=f'user{i}',
                password='password123'
            )
            users.append(user)

        posts = []
        for i in range(20):
            post = Post.objects.create(
                text=f'This is test post {i}',
                user=random.choice(users),
                timestamp=timezone.now()
            )
            posts.append(post)

        for post in posts:
            num_comments = random.randint(0, 5)
            for j in range(num_comments):
                Comment.objects.create(
                    text=f'Comment {j} on post {post.id}',
                    user=random.choice(users),
                    post=post,
                    timestamp=timezone.now()
                )

        self.stdout.write(self.style.SUCCESS('Successfully created test data'))