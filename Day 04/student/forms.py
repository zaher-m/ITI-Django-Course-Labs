

from django import forms
from course.models import Course

class StudentForm(forms.Form):
    name = forms.CharField(
        required=True, 
        min_length=3, 
        max_length=100, 
        label="Name"
    )
    age = forms.IntegerField(required=True, label="Age")
    image = forms.FileField(required=False, label="Profile Image")
    dob = forms.DateField(
        required=True, 
        label="Date of Birth",
        widget=forms.SelectDateWidget(years=range(2000, 2024))
    )
    courses = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        label="courses"
    )

    # populate courses 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['courses'].choices = [
            (course.code, f"{course.code} - {course.name}") for course in Course.objects.all()
        ]

    def clean_age(self):
        age = self.cleaned_data["age"]
        if age < 18:
            raise forms.ValidationError("Age must be at least 18")
        return age
