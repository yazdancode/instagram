from django.contrib import admin
from activity.models import Comment, Like


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("caption", "user", "post", "reply_to")
    search_fields = ["user", "post"]


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("user", "post")
    search_fields = ["user", "post"]
