from re import A
from django.contrib import admin
from .models import Book,Category


class BookAdmin(admin.ModelAdmin):
    list_display = ["name","author","get_category","uploader"]

    exclude =('uploader',)


    search_fields=('name','author')

    list_filter=('name','author')

    def get_category(self,obj):
        book = Book.objects.get(id=obj.id)
        print(book.category.all())
        return ",".join(value.name for value in book.category.all())

    get_category.short_description ="Categories"

    def save_model(self,request,obj,form,chang):
        obj.uploader = request.user.username
        return super(Book,self).save_model(request,obj,form,chang)

admin.site.register(Book,BookAdmin)
admin.site.register(Category)
