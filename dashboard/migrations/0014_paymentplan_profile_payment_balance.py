# Generated by Django 4.2.8 on 2024-07-24 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_remove_profile_payment_profile_payment_completed_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=500, null=True)),
                ('value', models.DecimalField(blank=True, decimal_places=2, help_text='Enter the percentage of the payment to make', max_digits=3, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='payment_balance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
