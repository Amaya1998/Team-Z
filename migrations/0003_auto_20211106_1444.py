# Generated by Django 3.2.8 on 2021-11-06 09:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_post_create_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Create_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='Comment',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='comment',
            name='Create_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Description',
            field=models.CharField(max_length=512),
        ),
    ]