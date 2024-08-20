from django.contrib import admin

from v1.bookmarks.models import Bookmark


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin): ...
