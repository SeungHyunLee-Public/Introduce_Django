from django.contrib import admin
from .models import *
from rangefilter.filter import DateRangeFilter, DateRangeFilter

# Register your models here.
#admin.site.register(Employee)
#admin.site.register(Building)
#admin.site.register(Visitor)


#from django.contrib.admin.models import LogEntry   // clear admin recent actions
#LogEntry.objects.all().delete()

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['empname', 'floor', 'uniname'] # 커스터마이징 코
    list_filter = ['empname', 'floor', 'uniname']
    list_per_page = 7
    search_fields = ['empname', 'floor', 'uniname']
admin.site.register(Employee, EmployeeAdmin)

class BuildingAdmin(admin.ModelAdmin):
    list_display = ['code', 'name'] # 커스터마이징 코
    list_filter = ['code', 'name']
    list_per_page = 7
    search_fields = ['code', 'name']
admin.site.register(Building, BuildingAdmin)

class VisitorAdmin(admin.ModelAdmin):
    list_display = ['visname', 'viscode', 'temp', 'uniname', 'visfloor'] # 커스터마이징 코
    list_filter = ['visname', 'viscode', 'temp', 'uniname', 'visfloor']
    list_per_page = 7
    search_fields = ['visname', 'viscode', 'temp', 'uniname', 'visfloor']
admin.site.register(Visitor, VisitorAdmin)


#class EmployeeAdmin(admin.ModelAdmin):
#    list_display = ['empname', 'floor', 'uniname']
#    list_filter = ('gender',
#        ('hire_date', DateRangeFilter),
#        ('birth_date', DateRangeFilter),
#    )
#    search_fields = ['empname', 'floor', 'uniname']