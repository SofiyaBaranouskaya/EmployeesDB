# Generated by Django 4.2.15 on 2024-10-07 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0010_alter_project_employees'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='disability',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='occupational_disease',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='political_party_membership',
        ),
        migrations.AlterField(
            model_name='project',
            name='employees',
            field=models.ManyToManyField(related_name='Проекты', to='employees.employee', verbose_name='Сотрудники'),
        ),
    ]
