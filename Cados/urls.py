from apps.api.views import api
from django.urls import re_path
from django.conf import settings
from django.contrib import admin
from django.views.static import serve
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path("admin/doc/", include("django.contrib.admindocs.urls")),
    path("admin/", admin.site.urls),
    path("api/", api.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    re_path(
        r"^media/(?P<path>.*)$",
        serve,
        {
            "document_root": settings.MEDIA_ROOT,
        },
    ),
]
