from django import forms
from .models import Employee, Attendance

EMPLOYEE_INPUT_CLASS = (
    "w-full rounded-lg border border-gray-300 px-4 py-2.5 text-sm "
    "focus:border-blue-500 focus:ring-2 focus:ring-blue-100 outline-none"
)

ATTENDANCE_INPUT_CLASS = (
    "w-full rounded-lg border border-gray-300 px-4 py-2.5 text-sm "
    "text-gray-900 bg-white "
    "focus:border-emerald-500 focus:ring-2 focus:ring-emerald-100 "
    "outline-none transition"
)


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {
            "employee_id": forms.TextInput(attrs={
                "class": EMPLOYEE_INPUT_CLASS,
                "placeholder": "EMP001",
                "required": True,
            }),
            "full_name": forms.TextInput(attrs={
                "class": EMPLOYEE_INPUT_CLASS,
                "placeholder": "John Doe",
                "required": True,
            }),
            "email": forms.EmailInput(attrs={
                "class": EMPLOYEE_INPUT_CLASS,
                "placeholder": "john@company.com",
                "required": True,
            }),
            "department": forms.TextInput(attrs={
                "class": EMPLOYEE_INPUT_CLASS,
                "placeholder": "Engineering",
                "required": True,
            }),
        }

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = "__all__"
        widgets = {
            "employee": forms.Select(
                attrs={
                    "class": ATTENDANCE_INPUT_CLASS,
                }
            ),
            "date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": ATTENDANCE_INPUT_CLASS,
                }
            ),
            "status": forms.Select(
                attrs={
                    "class": ATTENDANCE_INPUT_CLASS,
                }
            ),
        }

