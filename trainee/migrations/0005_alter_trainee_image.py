# Generated by Django 5.1.7 on 2025-03-19 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainee', '0004_trainee_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainee',
            name='image',
            field=models.ImageField(blank=True, default='default_trainee.png', null=True, upload_to='trainee/img/'),
        ),
    ]
