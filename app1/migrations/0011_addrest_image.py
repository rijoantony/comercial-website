# Generated by Django 4.1.5 on 2023-03-14 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_remove_addrest_first_name_remove_addrest_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='addrest',
            name='Image',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
