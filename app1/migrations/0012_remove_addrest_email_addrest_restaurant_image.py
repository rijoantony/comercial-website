# Generated by Django 4.1.5 on 2023-03-15 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_addrest_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addrest',
            name='Email',
        ),
        migrations.AddField(
            model_name='addrest',
            name='Restaurant_Image',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
