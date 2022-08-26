# Generated by Django 3.1.7 on 2022-08-25 14:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220825_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikel',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artikel',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='artikel',
            name='published',
            field=models.DateTimeField(null=True),
        ),
    ]