# Generated by Django 2.1.3 on 2018-11-08 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='choice',
            field=models.CharField(blank=True, choices=[('1', 'タスク'), ('2', 'アニメ'), ('3', '本'), ('4', 'ゲーム')], default=None, max_length=10),
        ),
    ]
