from enum import auto
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=125,verbose_name="Category Name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Book(models.Model):
    name = models.CharField(max_length=256,verbose_name='Book Name')
    book_cover = models.ImageField(upload_to='cover/',blank=True,verbose_name="Book cover")
    author = models.CharField(max_length=256,verbose_name="Author")
    published_date = models.DateField(verbose_name="Published Date")
    description = models.TextField(verbose_name="Description")
    download_url = models.URLField(verbose_name="Download URL")
    category = models.ManyToManyField(Category,related_name="book_category",verbose_name="Category")
    uploader = models.ForeignKey(User,verbose_name="Uploader",on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name

    
    class Meta:
        verbose_name = "Book"
        verbose_name_plural ="Books"