# Generated by Django 4.2.4 on 2023-08-03 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_user_date_off_alter_user_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_off',
            field=models.TimeField(auto_now_add=True, verbose_name='Оставшееся время'),
        ),
    ]
