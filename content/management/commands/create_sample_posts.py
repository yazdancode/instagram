from random import choice, sample, randint

from django.contrib.auth.models import User
from django.core.management import BaseCommand

from content.models import PostMedia, Post
from location.models import Location

SAMPLE_CAPTION = (
    "Lorem ipsum odor amet, consectetuer adipiscing elit. Semper eu ligula sapien porta integer"
    " aptent semper lobortis. Felis fermentum aliquam efficitur venenatis porttitor. "
    "Ornare malesuada lobortis curae integer mattis mollis lacus aptent. Nisi finibus ac est tortor,"
    " semper diam. Morbi sodales ligula amet ante felis morbi rhoncus dolor. Nibh tempor suspendisse porttitor;"
    " dui habitasse iaculis. Bibendum cras conubia torquent fames morbi duis."
)


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = User.objects.all()
        media_images = list(PostMedia.objects.all())
        locations = Location.objects.all()
        created_posts = []

        if not users or not locations:
            self.stdout.write(
                self.style.ERROR(
                    "No users or locations found. Please ensure your database has users and locations."
                )
            )
            return

        for i in range(200):
            post = Post.objects.create(
                user=choice(users), location=choice(locations), caption=SAMPLE_CAPTION
            )

            if media_images:
                post.media.add(
                    *sample(
                        media_images,
                        min(randint(1, len(media_images)), len(media_images)),
                    )
                )

            created_posts.append(post)

        self.stdout.write(self.style.SUCCESS(f"{len(created_posts)} posts created"))
