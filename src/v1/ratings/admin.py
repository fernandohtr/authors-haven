from django.contrib import admin

from v1.ratings.models import Rating


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "article",
        "rating",
        "created_at",
        "updated_at",
    ]
