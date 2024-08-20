from django.contrib import admin

from v1.responses.models import Response


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = [
        "pkid",
        "id",
        "user",
        "article",
        "parent_response",
        "content",
        "created_at",
    ]
    list_display_links = [
        "pkid",
        "id",
        "user",
    ]
