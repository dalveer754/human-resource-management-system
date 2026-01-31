from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Employee, Attendance
from .forms import EmployeeForm, AttendanceForm
from django.db.models import Count, Q

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
    date = request.GET.get("date")
    employee = request.GET.get("employee")
    status = request.GET.get("status")

    records = Attendance.objects.select_related("employee")

    if date:
        records = records.filter(date=date)

    if employee:
        records = records.filter(employee__full_name__icontains=employee)

    if status:
        records = records.filter(status__iexact=status)

    summary = Attendance.objects.filter(
        status__iexact="present"
    ).values(
        "employee__full_name"
    ).annotate(
        total_present=Count("id")
    )

    return render(request, "attendance_records.html", {
        "records": records,
        "summary": summary,
        "selected_date": date,
        "selected_employee": employee,
        "selected_status": status,
    })



def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    messages.success(request, "Employee removed successfully")
    return redirect("/employees/")


def dashboard(request):
    total_employees = Employee.objects.count()
    total_records = Attendance.objects.count()
    total_present = Attendance.objects.filter(status="Present").count()
    total_absent = Attendance.objects.filter(status="Absent").count()

    return render(request, "dashboard.html", {
        "total_employees": total_employees,
        "total_records": total_records,
        "total_present": total_present,
        "total_absent": total_absent,
    })
