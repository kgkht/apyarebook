# Generated by Django 2.2.12 on 2020-05-25 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebooks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ebook',
            name='source_file',
            field=models.FileField(default='', upload_to='pdf/'),
        ),
    ]