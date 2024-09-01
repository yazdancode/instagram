from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from content.models import Post
from lib.common_models import BaseModel

User = get_user_model()


class Comment(BaseModel):
    """
    A model representing a comment on a post.

    Attributes:
        caption (TextField): The text content of the comment.
        user (ForeignKey): The user who posted the comment.
        post (ForeignKey): The post to which the comment is attached.
        reply_to (ForeignKey): The comment to which this comment is a reply.

    Methods:
        __str__(self): Returns a string representation of the comment, displaying its caption.
    """
    caption = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    reply_to = models.ForeignKey(
        "self", related_name="replies", on_delete=models.CASCADE, null=True, blank=True
    )

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return self.caption


class Like(BaseModel):
    """
    A model representing a like on a post.

    Attributes:
        user (ForeignKey): The user who liked the post.
        post (ForeignKey): The post that was liked.

    Methods:
        __str__(self): Returns a string representation of the like, displaying the user and post IDs.

    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")

    class Meta:
        verbose_name = _("Like")
        verbose_name_plural = _("Likes")
        unique_together = ("user", "post")

    def __str__(self):
        return f"{self.user.username} >> {self.post.id}"
