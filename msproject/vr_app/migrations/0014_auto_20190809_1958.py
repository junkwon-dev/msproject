# Generated by Django 2.2.3 on 2019-08-09 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vr_app', '0013_auto_20190809_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='sms',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
