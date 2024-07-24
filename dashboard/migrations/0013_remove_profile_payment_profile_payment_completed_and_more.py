# Generated by Django 4.2.8 on 2024-07-24 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0012_profile_payment_courseschedule_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='payment',
        ),
        migrations.AddField(
            model_name='profile',
            name='payment_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candidate', to=settings.AUTH_USER_MODEL),
        ),
    ]
