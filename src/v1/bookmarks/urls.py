from django.urls import path

from v1.bookmarks.views import BookmarkCreateView

urlpatterns = [
    path("bookmark_article/<uuid:article_id>/", BookmarkCreateView.as_view(), name="bookmark_article"),
    path("remove_bookmark/<uuid:article_id>/", BookmarkCreateView.as_view(), name="remove_bookmark"),
]
