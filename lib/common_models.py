from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_time = models.DateTimeField(_("created_time"), auto_now_add=True)
    modified_time = models.DateTimeField(_("modified_time"), auto_now_add=True)

    class Meta:
        abstract = True
