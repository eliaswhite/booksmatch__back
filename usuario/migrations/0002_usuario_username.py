# Generated by Django 4.2.7 on 2023-11-21 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
