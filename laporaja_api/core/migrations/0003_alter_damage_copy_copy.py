# Generated by Django 3.2.3 on 2021-06-02 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_user_id')
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='damage_type',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
         migrations.AlterField(
            model_name='report',
            name='damage_severity',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
    ]
