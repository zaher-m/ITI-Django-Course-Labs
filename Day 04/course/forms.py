from django import forms

class CourseForm(forms.Form):
    code = forms.CharField(max_length=50,required=True,label="Course Code")
    name = forms.CharField(max_length=100,required=True,label="Course Name")

