# Generated by Django 3.0.7 on 2020-06-29 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0021_auto_20200628_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='developerinfo',
            name='raing',
            field=models.ImageField(default='0', max_length=4, upload_to=''),
        ),
    ]
