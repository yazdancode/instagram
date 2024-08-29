from django.contrib import admin

from activity.models import Comment, Like


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ("caption", "user", "post", "reply_to")
=======
    list_display = (("caption", "user", "post", "reply_to"),)
>>>>>>> secods-branch
    search_fields = ["user", "post"]


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ("user", "post")
=======
    list_display = (("user", "post"),)
>>>>>>> secods-branch
    search_fields = ["user", "post"]
