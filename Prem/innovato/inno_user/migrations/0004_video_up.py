# Generated by Django 3.1.2 on 2021-03-05 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inno_user', '0003_auto_20210304_2048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video_up',
            fields=[
                ('v_id', models.AutoField(primary_key=True, serialize=False)),
                ('v_title', models.CharField(default='', max_length=30)),
                ('v_file', models.FileField(upload_to='inno_user/videos')),
                ('v_desc', models.CharField(default='', max_length=120)),
            ],
        ),
    ]
