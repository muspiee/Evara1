# Generated by Django 5.0.2 on 2024-04-05 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_alter_subcategory_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_favorite',
            new_name='is_Favorite',
        ),
        migrations.AddField(
            model_name='product',
            name='is_Featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='is_New',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='is_Popular',
            field=models.BooleanField(default=False),
        ),
    ]
