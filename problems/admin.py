from django.contrib import admin
from .models import Problems, Categories

@admin.register(Problems)
class ProblemsAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'category', 'user']  # Поля для отображения
    list_filter = ['status', 'category']  # Фильтры
    search_fields = ['name', 'description', 'user__username']  # Поля для поиска
    list_editable = ['status']  # Позволяет редактировать статус прямо в списке
    readonly_fields = ['user', 'image']  # Поля только для чтения
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'address', 'category', 'status', 'user')
        }),
        ('Изображения', {
            'fields': ('image', 'image_resolved'),
        }),
    )

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}  # Автозаполнение slug
