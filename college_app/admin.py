from django.contrib import admin
from college_app.models import Department,Teachers,Students
# Register your models here.

class Department_Admin(admin.ModelAdmin):
    list_display=['d_id','d_name']

admin.site.register(Department,Department_Admin)


class Faculty_admin(admin.ModelAdmin):
    list_display=['f_id','f_name','f_dep']

admin.site.register(Teachers,Faculty_admin)


class Student_admin(admin.ModelAdmin):
    list_display=['s_id','s_name','s_dep']


admin.site.register(Students,Student_admin)