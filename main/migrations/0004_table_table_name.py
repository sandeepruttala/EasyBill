# Generated by Django 4.2.6 on 2024-01-23 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_item_table_status_orderhistory_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='table_name',
            field=models.CharField(default='Table<django.db.models.fields.IntegerField>', max_length=100),
        ),
    ]
