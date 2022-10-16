from django.conf import settings
from django.urls import re_path
from django.views.static import serve

from apps.api.views import api
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/doc/", include("django.contrib.admindocs.urls")),
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]

urlpatterns += [
    re_path(
        r"^media/(?P<path>.*)$",
        serve,
        {
            "document_root": settings.MEDIA_ROOT,
        },
    ),
]
