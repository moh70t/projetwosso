# Generated by Django 5.0.6 on 2024-06-25 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_product_categorie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='label',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]