# Generated by Django 3.1.4 on 2020-12-14 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BackEndThings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_name', models.CharField(max_length=100)),
                ('source_folder', models.CharField(max_length=100)),
                ('old_file_format', models.CharField(max_length=6)),
                ('new_file_format', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='DataBaseUPdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
