# Generated by Django 4.1.3 on 2022-12-01 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='img/FSDI_Final_Logo.svg', upload_to='static/img'),
        ),
    ]
