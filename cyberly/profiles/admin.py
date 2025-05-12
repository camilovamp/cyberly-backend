from django.contrib import admin
from .models import Language, Category

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    ordering = ['name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_featured']
    search_fields = ['name']
    list_filter = ['is_featured']
    ordering = ['name']
