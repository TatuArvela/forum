# Generated by Django 3.0.3 on 2020-02-25 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0002_auto_20200225_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='edited_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='edited_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
