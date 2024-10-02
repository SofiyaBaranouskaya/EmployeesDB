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
    union_membership = models.BooleanField(default=False, verbose_name='Членство в профсоюзе')
    political_party_membership = models.CharField(max_length=255, blank=True, null=True, verbose_name='Членство в политической партии')
    occupational_disease = models.CharField(max_length=255, blank=True, null=True, verbose_name='Профессиональное заболевание')
    disability = models.CharField(
        max_length=1,
        choices=[
            ('-', 'Нет'),
            ('1', '1 группа'),
            ('2', '2 группа'),
            ('3', '3 группа'),
        ],
        default='-',
        verbose_name='Инвалидность'
    )
    additional_info = models.TextField(blank=True, null=True, verbose_name='Дополнительная информация')
    class Meta:
        verbose_name = "Сотрудника"
        verbose_name_plural = "Сотрудники"
    def __str__(self):
        return self.fio

class Manager(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО')
    department = models.CharField(max_length=100, verbose_name='Отдел')
    employees = models.ManyToManyField(Employee, related_name='Руководители', verbose_name='Сотрудники')
    class Meta:
        verbose_name = "Руководителя"
        verbose_name_plural = "Руководители"

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    company = models.CharField(max_length=100, verbose_name='Компания-заказчик')
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, verbose_name='Руководитель')
    employees = models.ManyToManyField(Employee, related_name='Проекты', verbose_name='Сотрудники')

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.name