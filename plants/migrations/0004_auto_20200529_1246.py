# Generated by Django 3.0.6 on 2020-05-29 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0003_auto_20200529_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image_url',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='userplant',
            name='image_url',
            field=models.URLField(blank=True, default=''),
        ),
    ]
