# Generated by Django 5.0.2 on 2024-02-23 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_phone_alter_user_referral_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='referral_code',
            field=models.CharField(default='5xC6GZ', max_length=6, verbose_name='Реферальный код пользователя'),
        ),
    ]