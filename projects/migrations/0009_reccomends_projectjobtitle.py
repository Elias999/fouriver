# Generated by Django 3.0.6 on 2020-06-22 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20200622_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='reccomends',
            name='projectjobtitle',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
