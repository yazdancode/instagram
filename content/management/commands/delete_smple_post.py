from django.core.management.base import BaseCommand
from django.utils import timezone
from content.models import Post
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Delete posts based on criteria"

    def add_arguments(self, parser):
        parser.add_argument(
            "--user-id",
            type=int,
            help="Specify the user ID to delete posts for",
        )
        parser.add_argument(
            "--older-than-days",
            type=int,
            help="Delete posts older than a specified number of days",
        )
        parser.add_argument(
            "--all",
            action="store_true",
            help="Delete all posts",
        )

    def handle(self, *args, **options):
        user_id = options.get("user_id")
        older_than_days = options.get("older_than_days")
        delete_all = options.get("all")

        posts_to_delete = Post.objects.all()

        if user_id:
            try:
                user = User.objects.get(pk=user_id)
                posts_to_delete = posts_to_delete.filter(user=user)
            except User.DoesNotExist:
                self.stdout.write(
                    self.style.ERROR(f"User with ID {user_id} does not exist.")
                )
                return

        if older_than_days:
            cutoff_date = timezone.now() - timezone.timedelta(days=older_than_days)
            posts_to_delete = posts_to_delete.filter(created_at__lt=cutoff_date)

        if not delete_all and not user_id and not older_than_days:
            self.stdout.write(
                self.style.ERROR(
                    "You must specify at least one option: --user-id, --older-than-days, or --all"
                )
            )
            return

        deleted_count, _ = posts_to_delete.delete()
        self.stdout.write(
            self.style.SUCCESS(f"Successfully deleted {deleted_count} posts.")
        )
