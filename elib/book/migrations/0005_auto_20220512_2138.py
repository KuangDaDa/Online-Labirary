# Generated by Django 2.2 on 2022-05-12 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20220512_2133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='upload_date',
        ),
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.DateField(verbose_name='Published Date'),
        ),
    ]
