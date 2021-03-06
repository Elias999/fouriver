# Generated by Django 3.0.6 on 2020-06-21 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_projects_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='offers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('developername', models.CharField(max_length=100, null=True)),
                ('projectid', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('money', models.IntegerField()),
            ],
            options={
                'db_table': 'offers',
            },
        ),
    ]
