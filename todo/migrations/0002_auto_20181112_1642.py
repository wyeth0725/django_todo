# Generated by Django 2.1.3 on 2018-11-12 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='時間',
        ),
        migrations.AddField(
            model_name='todo',
            name='notice',
            field=models.DateField(blank=True, null=True),
        ),
    ]