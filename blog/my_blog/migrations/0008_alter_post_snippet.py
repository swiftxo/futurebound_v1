# Generated by Django 5.0.4 on 2024-05-01 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0007_post_snippet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(blank=True, max_length=155),
        ),
    ]
