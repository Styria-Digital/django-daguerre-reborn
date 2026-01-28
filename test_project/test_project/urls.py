from django.urls import include, re_path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    re_path(r'^', include('daguerre.urls')),
]
