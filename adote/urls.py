from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("users.urls"), name="cadastro"),
    path("admin/", admin.site.urls),
    path("auth/", include("users.urls")),
    path("divulgar/", include("divulgar.urls")),
    path("adotar/", include("adotar.urls")),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
