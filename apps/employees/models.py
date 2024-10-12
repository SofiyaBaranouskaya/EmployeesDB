from django.db import models

class Employee(models.Model):
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    birth_date = models.DateField(verbose_name='Дата рождения')
    education = models.CharField(max_length=100, verbose_name='Образование')
    qualification = models.CharField(max_length=100, verbose_name='Квалификация')
    department = models.CharField(max_length=100, verbose_name='Отделение')
    work_experience = models.IntegerField(verbose_name='Стаж работы')
    salary = models.IntegerField(verbose_name='Заработная плата, BYN', default='2000')
    union_membership = models.BooleanField(default=False, verbose_name='Членство в профсоюзе')
    additional_info = models.TextField(blank=True, null=True, verbose_name='Дополнительная информация')
    class Meta:
        verbose_name = "Сотрудника"
        verbose_name_plural = "Сотрудники"
    def __str__(self):
        return f"{self.fio} ({self.qualification})"

class Manager(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО')
    department = models.CharField(max_length=100, verbose_name='Отдел')
    employees = models.ManyToManyField(Employee, related_name='managers', verbose_name='Сотрудники')
    class Meta:
        verbose_name = "Заведующего"
        verbose_name_plural = "Заведующие отделами"

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=200, verbose_name='Описание', default="-")
    company = models.CharField(max_length=100, verbose_name='Заказчик')
    manager = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Руководитель', limit_choices_to={'qualification': 'Менеджер проектов'})
    employees = models.ManyToManyField(Employee, related_name='Проекты', verbose_name='Сотрудники')

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.name


