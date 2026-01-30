from django.contrib import admin
from .models import Employee, Attendance

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("employee_id", "full_name", "email", "department")
    search_fields = ("employee_id", "full_name", "email", "department")
    list_filter = ("department",)
    
@admin.register(Attendance)

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("employee", "date", "status")
    search_fields = ("employee__full_name", "employee__employee_id")
    list_filter = ("status", "date")    
