# Generated by Django 4.2.4 on 2023-10-02 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authority', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='accesstimeoutlogs',
            table='sys_access_timeout_logs',
        ),
        migrations.AlterModelTable(
            name='oplogs',
            table='sys_operation_logs',
        ),
    ]
