# Generated by Django 4.2.2 on 2023-08-07 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredients',
            name='id',
        ),
        migrations.AddField(
            model_name='ingredients',
            name='new_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
