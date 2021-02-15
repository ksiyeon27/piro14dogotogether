from django.contrib import admin
from .models import placeAddByUser

@admin.register(placeAddByUser)
class PlaceAddedByUser(admin.ModelAdmin):
    list_display = ('name', 'region', 'xmap', 'ymap', 'category', 'created_at', 'created_by')
    list_filter = ('created_at', 'region', 'category')
    search_fields = ('name', 'region', 'category')

    def get_queryset(self, request):
        return super().get_queryset('category')