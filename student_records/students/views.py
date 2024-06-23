from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm

# Index view to list all students
def index(request):
    students = Student.objects.all()
    print(students)  # For debugging purposes
    return render(request, 'students/index.html', {'students': students})

# Get student information
def student_info(request, pk):  # pk (primary key; a unique identifier for students)
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/info.html', {'student': student})

# Create a new student
def create_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm()
    return render(request, 'students/form.html', {'form': form})

# Update an existing student information 
def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/form.html', {'form': form})

# Deleete and existing student information
def confirm_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect('index')
    return render(request, 'students/confirm_delete.html', {'student': student})



