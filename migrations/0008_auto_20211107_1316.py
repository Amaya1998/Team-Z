# Generated by Django 3.2.8 on 2021-11-07 07:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0007_alter_comment_create_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='Commenter_name',
            field=models.CharField(default='Jane Doe', max_length=512),
        ),
        migrations.AlterField(
            model_name='comment',
            name='Create_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
