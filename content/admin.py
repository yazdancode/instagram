from django.contrib import admin
from django.contrib.admin import register
from content.models import Post, PostMedia, Tag, PostTag, TaggedUser


register(Post)


class PostAdmin(admin.ModelAdmin):
    list_display = ("caption", "user", "location")
    search_fields = ["user"]


@register(PostMedia)
class PostMediaAdmin(admin.ModelAdmin):
    list_display = ("IMAGE", "VIDEO", "media_type", "post", "media_file")
    search_fields = ["IMAGE", "VIDEO"]


@register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ["title"]


@register(PostTag)
class PostTagAdmin(admin.ModelAdmin):
    list_display = ("post", "tag")
    search_fields = ["post"]


@register(TaggedUser)
class TaggedUserAdmin(admin.ModelAdmin):
    list_display = ["user", "post"]
    search_fields = ["post"]
