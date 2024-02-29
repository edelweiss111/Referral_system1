# Generated by Django 5.0.2 on 2024-02-19 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_referral_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.BigIntegerField(unique=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='user',
            name='referral_code',
            field=models.CharField(default='dwdnEU', max_length=6, verbose_name='Реферальный код пользователя'),
        ),
    ]