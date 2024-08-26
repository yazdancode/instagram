from django.db import models
from django.utils.translation import gettext_lazy as _
from lib.common_models import BaseModel


class Location(BaseModel):
    title = models.CharField(_("title"), max_length=32)
    points = models.JSONField(_("points"))

    class Meta:
        verbose_name = _("Location")
        verbose_name_plural = _("Locations")

    def __str__(self):
        return self.title
