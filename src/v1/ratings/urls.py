from django.urls import path

from v1.ratings.views import RatingsCreateView

urlpatterns = [path("rate_article/<uuid:article_id>/", RatingsCreateView.as_view(), name="rating_create")]
