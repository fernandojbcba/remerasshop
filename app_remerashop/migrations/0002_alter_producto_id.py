# Generated by Django 4.2.2 on 2023-07-04 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_remerashop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
