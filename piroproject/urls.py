
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('community/', include('blog.urls')),
    path('', include('accounts.urls')),
    path('sociallogin/', include('allauth.urls')),
    path('map/',include('map.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
