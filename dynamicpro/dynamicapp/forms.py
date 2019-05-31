from django import forms
from .models import Student, Teacher, Grade, Course

class studentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'



class teacherForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields='__all__'


class courseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields='__all__'        


class gradeForm(forms.ModelForm):
    class Meta:
        model=Grade
        fields='__all__' 