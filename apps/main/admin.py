from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Books)
class BookRegister(admin.ModelAdmin):
   list_display=["id",'title','pages','logo']
   list_filter=['id','title','created_at']
   search_fields=["id",'title','pages','logo','created_at']

   



