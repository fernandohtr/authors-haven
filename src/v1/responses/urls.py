from django.urls import path

from v1.responses.views import ResponseUpdateDeleteView, ResponsListCreateView

urlpatterns = [
    path("articles/<uuid:article_id>/", ResponsListCreateView.as_view(), name="article_responses"),
    path("<uuid:id>/", ResponseUpdateDeleteView.as_view(), name="response_detail"),
]
