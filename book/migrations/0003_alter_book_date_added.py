# Generated by Django 4.2.1 on 2023-05-19 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_book_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_added',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
