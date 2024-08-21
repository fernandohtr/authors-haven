from django_elasticsearch_dsl_drf.filter_backends import (
    DefaultOrderingFilterBackend,
    FilteringFilterBackend,
    IdsFilterBackend,
    OrderingFilterBackend,
    SearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from rest_framework import permissions

from v1.search.documents import ArticleDocument
from v1.search.serializers import ArticleElasticSearchSerializer


class ArticleElasticSearchView(DocumentViewSet):
    document = ArticleDocument
    serializer_class = ArticleElasticSearchSerializer
    lookup_field = "id"
    permission_classes = [permissions.AllowAny]
    filter_backends = [
        DefaultOrderingFilterBackend,
        FilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        SearchFilterBackend,
    ]
    search_fields = (
        "title",
        "description",
        "body",
        "author_first_name",
        "author_last_name",
        "tags",
    )
    filter_fields = {
        "slug": "slug.raw",
        "tags": "tags",
        "created_at": "created_at",
    }
    ordering_fields = {
        "created_at": "created_at",
    }
    ordering = ("-created_at",)
