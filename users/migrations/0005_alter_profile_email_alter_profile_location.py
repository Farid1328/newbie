# Generated by Django 4.0.4 on 2022-06-13 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_username1_bio_remove_username1_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
