from django.contrib import admin
from .models import Ebook, Category, Series
# Register your models here.

class EbookAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'series', 'pub_date')

admin.site.register(Ebook, EbookAdmin)
admin.site.register(Category)
admin.site.register(Series)
