# Generated by Django 2.2 on 2021-08-28 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción de compañia'),
        ),
    ]
