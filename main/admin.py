from django.contrib import admin
from problems.models import Categories, Problems


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}


@admin.register(Problems)
class ProblemsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}
