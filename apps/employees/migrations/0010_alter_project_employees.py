# Generated by Django 4.2.15 on 2024-10-07 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0009_alter_manager_options_alter_manager_employees_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='employees',
            field=models.ManyToManyField(limit_choices_to=models.Q(('qualification', 'Менеджер проектов'), ('id__ne', models.F('manager')), _connector='OR'), related_name='projects', to='employees.employee', verbose_name='Сотрудники'),
        ),
    ]
