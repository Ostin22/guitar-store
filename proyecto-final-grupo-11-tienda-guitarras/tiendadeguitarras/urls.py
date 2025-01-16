from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from tiendadeguitarras import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('guitars.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)