from django import forms
from .models import Employee, Project
from django_select2.forms import Select2MultipleWidget

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['fio', 'address', 'phone', 'birth_date', 'education', 'qualification', 'department', 'work_experience', 'union_membership', 'political_party_membership', 'disability', 'occupational_disease', 'additional_info']

class ProjectForm(forms.ModelForm):
    employees = forms.ModelMultipleChoiceField(
        queryset=Employee.objects.all(),
        widget=Select2MultipleWidget(attrs={'data-minimum-input-length': 1})
    )

    class Meta:
        model = Project
        fields = ['name', 'company', 'manager', 'employees']