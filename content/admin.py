from django.contrib import admin
from content.models import Post, PostMedia, Tag, PostTag, TaggedUser


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("caption", "user", "location")
    search_fields = ["user"]


@admin.register(PostMedia)
class PostMediaAdmin(admin.ModelAdmin):
    list_display = ("IMAGE", "VIDEO", "media_type", "post", "media_file")
    search_fields = ["IMAGE", "VIDEO"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ["title"]


@admin.register(PostTag)
class PostTagAdmin(admin.ModelAdmin):
    list_display = ("post", "tag")
    search_fields = ["post"]


@admin.register(TaggedUser)
class TaggedUserAdmin(admin.ModelAdmin):
    list_display = ["user", "post"]
    search_fields = ["post"]
