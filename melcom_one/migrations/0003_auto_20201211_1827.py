# Generated by Django 3.1.4 on 2020-12-11 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('melcom_one', '0002_remove_video_videofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
