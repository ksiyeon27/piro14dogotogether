from django.contrib import admin
from .models import placeAddByUser

@admin.register(placeAddByUser)
class PlaceAddedByUser(admin.ModelAdmin):
    list_display = ('name', 'region', 'xmap', 'ymap', 'created_at', 'created_by')
    list_filter = ('created_at', 'region')
    search_fields = ('name', 'region')

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('region')
