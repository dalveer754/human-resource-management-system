from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("add_employees/", views.add_employee, name="add_employee"),
    path("employees/", views.employee_records, name="employee_records"),

    path("attendance/", views.mark_attendance, name="mark_attendance"),
    path("attendance-records/", views.attendance_records, name="attendance_records"),

    path("delete/<int:pk>/", views.delete_employee, name="delete_employee"),
]
