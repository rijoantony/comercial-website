# Generated by Django 4.1.5 on 2023-03-15 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_viewrest'),
    ]

    operations = [
        migrations.CreateModel(
            name='addmenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Restaurant_Name', models.CharField(max_length=50)),
                ('Menu_Name', models.CharField(max_length=50)),
                ('Image', models.CharField(max_length=500)),
                ('cuisin', models.CharField(max_length=50)),
                ('Type', models.CharField(max_length=50)),
            ],
        ),
    ]