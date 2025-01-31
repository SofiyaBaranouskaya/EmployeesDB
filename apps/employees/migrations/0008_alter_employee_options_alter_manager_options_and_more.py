# Generated by Django 4.2.15 on 2024-10-07 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0007_alter_employee_department'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Сотрудника', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.AlterModelOptions(
            name='manager',
            options={'verbose_name': 'Руководителя', 'verbose_name_plural': 'Руководители'},
        ),
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.CharField(default='-', max_length=200, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='department',
            field=models.CharField(max_length=100, verbose_name='Отдел'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='employees',
            field=models.ManyToManyField(related_name='Руководители', to='employees.employee', verbose_name='Сотрудники'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='name',
            field=models.CharField(max_length=100, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='project',
            name='company',
            field=models.CharField(max_length=100, verbose_name='Заказчик'),
        ),
        migrations.AlterField(
            model_name='project',
            name='employees',
            field=models.ManyToManyField(related_name='Проекты', to='employees.employee', verbose_name='Сотрудники'),
        ),
        migrations.AlterField(
            model_name='project',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.manager', verbose_name='Руководитель'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
    ]
