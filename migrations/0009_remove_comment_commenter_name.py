# Generated by Django 3.2.8 on 2021-11-07 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20211107_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='Commenter_name',
        ),
    ]