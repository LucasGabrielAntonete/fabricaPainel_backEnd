# Generated by Django 5.0.6 on 2024-07-18 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fabrica_painel', '0003_alter_ods_name_remove_work_ods_work_ods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='field',
            field=models.ManyToManyField(default=None, to='fabrica_painel.field'),
        ),
    ]