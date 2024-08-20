from dj_rest_auth.views import PasswordResetConfirmView
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from v1.users.views import CustomUserDetailsView

DJANGO_URLS = [
    path(settings.ADMIN_URL, admin.site.urls),
]
DRF_SPECTACULAR_URLS = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
LOCAL_URLS = [
    path("api/v1/auth/", include("dj_rest_auth.urls")),
    path("api/v1/auth/users/", CustomUserDetailsView.as_view(), name="user_detail"),
    path("api/v1/auth/registration/", include("dj_rest_auth.registration.urls")),
    path(
        "api/v1/auth/password/reset/confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path("api/v1/profiles/", include("v1.profiles.urls")),
    path("api/v1/articles/", include("v1.articles.urls")),
    path("api/v1/ratings/", include("v1.ratings.urls")),
    path("api/v1/bookmarks/", include("v1.bookmarks.urls")),
]

urlpatterns = DJANGO_URLS + DRF_SPECTACULAR_URLS + LOCAL_URLS

admin.site.site_header = "Authors Haven API Admin"
admin.site.site_title = "Authors Haven API Admin Portal"
admin.site.index_title = "Welcome to Authors Haven API Portal"
