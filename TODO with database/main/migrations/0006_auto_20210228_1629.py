# Generated by Django 3.1.1 on 2021-02-28 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210228_1621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='mark',
            new_name='list_id',
        ),
        migrations.RemoveField(
            model_name='todolist',
            name='name',
        ),
        migrations.AddField(
            model_name='todo',
            name='category',
            field=models.CharField(default='Incomplete', max_length=40),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]