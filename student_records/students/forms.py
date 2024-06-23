from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'email', 'phone', 'location', 'hobby']
        labels = {
          'first_name': 'First Name',
          'last_name': 'Last Name',
          'age': 'Age',
          'email': 'Email',
          'phone': 'Phone',
          'location': 'Location',
          'hobby': 'Hobby'
      }
      
