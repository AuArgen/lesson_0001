from django.contrib import admin

from books.models import Book


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published')
    list_filter = ('published',)
    search_fields = ('title',)