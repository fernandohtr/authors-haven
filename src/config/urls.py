from django.conf import settings
from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

DRF_SPECTACULAR_URLS = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
] + DRF_SPECTACULAR_URLS

admin.site.site_header = "Authors Haven API Admin"
admin.site.site_title = "Authors Haven API Admin Portal"
admin.site.index_title = "Welcome to Authors Haven API Portal"
