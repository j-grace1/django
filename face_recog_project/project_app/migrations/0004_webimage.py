# Generated by Django 4.1 on 2022-09-04 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0003_remove_uploadimage_caption'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=99999999999999999999999999)),
            ],
        ),
    ]