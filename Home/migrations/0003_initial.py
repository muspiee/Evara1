# Generated by Django 5.0.2 on 2024-04-05 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Home', '0002_delete_promote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ttile', models.CharField(max_length=20)),
                ('title1', models.CharField(max_length=20)),
                ('title2', models.CharField(max_length=20)),
                ('title3', models.CharField(max_length=20)),
                ('title4', models.CharField(max_length=20)),
                ('image', models.ImageField(default='null.png', upload_to='promote/')),
            ],
        ),
    ]
