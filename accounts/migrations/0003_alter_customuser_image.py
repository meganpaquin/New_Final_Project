# Generated by Django 4.1.3 on 2022-12-01 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_options_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='img/FSDI_Final_Logo.svg', upload_to='img'),
        ),
    ]