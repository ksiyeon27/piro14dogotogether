
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('community/', include('blog.urls', namespace='커뮤니티')),
    path('', include('accounts.urls')),
    path('sociallogin/', include('allauth.urls')),
    path('map/',include('map.urls')),
    path('calculator/', include('calculator.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
