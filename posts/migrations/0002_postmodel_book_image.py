# Generated by Django 5.0.1 on 2024-02-24 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='book_image',
            field=models.ImageField(blank=True, null=True, upload_to='./book-images/'),
        ),
    ]
