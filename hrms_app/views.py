from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Employee, Attendance
from .forms import EmployeeForm, AttendanceForm


def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee added successfully")
            return redirect("add_employee")  # 👈 redirect clears form
    else:
        form = EmployeeForm()  # empty form on GET

    return render(request, "employees.html", {
        "form": form
    })


def employee_records(request):
    employees = Employee.objects.all()
    return render(request, "employee_records.html", {
        "employees": employees
    })


def mark_attendance(request):
    form = AttendanceForm()
    records = Attendance.objects.select_related("employee").all()

    if request.method == "POST":
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Attendance saved")
            return redirect("/attendance/")
        else:
            messages.error(request, "Please correct the errors below")

    return render(request, "attendance.html", {
        "form": form
    })


def attendance_records(request):
    records = Attendance.objects.select_related("employee").all()
    return render(request, "attendance_records.html", {
        "records": records
    })


def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    messages.success(request, "Employee removed successfully")
    return redirect("/employees/")
