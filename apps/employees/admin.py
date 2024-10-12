from django.contrib import admin
from .models import Employee, Project, Manager
from django.contrib.auth.models import User, Group

admin.site.unregister(User)
admin.site.unregister(Group)


class YourModelAdmin(admin.ModelAdmin):
    list_display = ('fio', 'address', 'phone', 'birth_date', 'education', 'qualification', 'department', 'work_experience', 'salary', 'union_membership', 'additional_info')
    list_filter = ('qualification', 'department', 'work_experience', 'union_membership')
    search_fields = ('fio', 'department')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'manager')
    search_fields = ('name', 'company')
    filter_horizontal = ('employees',)

class ManagerAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')
    search_fields = ('name',)
    filter_horizontal = ('employees',)

admin.site.register(Employee, YourModelAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Manager, ManagerAdmin)

