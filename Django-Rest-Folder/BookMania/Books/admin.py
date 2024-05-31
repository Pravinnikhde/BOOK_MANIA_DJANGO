from django.contrib import admin
from .models import BookModel



class BookModelAdmin(admin.ModelAdmin):
    list_display=['id','bookname','authname','description']
admin.site.register(BookModel,BookModelAdmin)
