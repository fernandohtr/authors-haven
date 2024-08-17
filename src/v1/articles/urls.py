from django.urls import path

from v1.articles.views import ArticleListCreateView, ArticleRetrieveUpdateDestroyView

urlpatterns = [
    path("", ArticleListCreateView.as_view(), name="article_list_create"),
    path("<uuid:id>/", ArticleRetrieveUpdateDestroyView.as_view(), name="article_retrieve_update_destroy"),
]
