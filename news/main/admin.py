from django.contrib import admin
from .models import Category,New

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name'
    ]
    class Meta:
        model = Category

@admin.register(New)
class NewsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'category',
        'subject',
        'content',
        'file',
    ]

    class Meta:
       model = New


