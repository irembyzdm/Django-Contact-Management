# Generated by Django 5.0.3 on 2024-04-10 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_gelenarama_sirket_remove_order_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gelenarama',
            name='aciklama',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='gelenarama',
            name='arama_nedeni',
            field=models.TextField(),
        ),
    ]