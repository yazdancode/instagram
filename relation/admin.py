from django.contrib import admin

from relation.models import Relation


@admin.register(Relation)
class RelationAdmin(admin.ModelAdmin):
    list_display = ["from_user", "to_user"]
    search_fields = ["from_user", "to_user"]
