
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from uroki_povtor import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cafe.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
