# Generated by Django 3.2.8 on 2021-11-07 07:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0006_remove_comment_commenter_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='Create_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
