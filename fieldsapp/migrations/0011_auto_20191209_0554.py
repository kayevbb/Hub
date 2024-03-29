# Generated by Django 2.2.8 on 2019-12-09 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fieldsapp', '0010_auto_20191208_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.CharField(default=1, max_length=50, verbose_name='Email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='number',
            field=models.CharField(default=1, max_length=20, verbose_name='Телефон'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='username',
            field=models.CharField(default=1, max_length=70, verbose_name='ФИО'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='date_pub',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
