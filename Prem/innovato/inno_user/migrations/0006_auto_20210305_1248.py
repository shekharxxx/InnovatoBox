# Generated by Django 3.1.2 on 2021-03-05 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inno_user', '0005_auto_20210305_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video_up',
            name='v_file',
            field=models.FileField(upload_to='inno_user/videos/'),
        ),
    ]