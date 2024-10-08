# Generated by Django 5.1.1 on 2024-10-08 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0013_alter_booking_service'),
        ('services', '0004_alter_service_id_alter_servicetype_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='service',
            field=models.ManyToManyField(related_name='bookings', to='services.service'),
        ),
    ]
