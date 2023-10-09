
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from uroki_povtor import settings
from account.views import RegisterUser, LoginUser, logout_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cafe.urls')),
    path('manager/', include('manager.urls')),

    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
