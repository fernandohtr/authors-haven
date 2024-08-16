import django_filters

from v1.articles.models import Article


class ArticleFilter(django_filters.FilterSet):
    author = django_filters.CharFilter(field_name="author__first_name", lookup_expr="icontains")
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains")
    tags = django_filters.CharFilter(field_name="tags__name", lookup_expr="iexact")
    created_at = django_filters.DateFromToRangeFilter(field_name="created_at")
    updated_at = django_filters.DateFromToRangeFilter(field_name="updated_at")

    class Meta:
        model = Article
        fields = [
            "author",
            "title",
            "tags",
            "created_at",
            "updated_at",
        ]
