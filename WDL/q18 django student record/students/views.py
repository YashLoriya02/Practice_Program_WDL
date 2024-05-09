from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.contrib import messages

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, "User Deleted Successfully.")
        return redirect('/')

def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {"data" : students})

def create(request):
    if request.method == "POST" :
        name = request.POST.get('name','')
        sap = request.POST.get('sap','')
        age =  request.POST.get('age','')
        grade =  request.POST.get('grade','')
        student = Student(name=name, sap=sap ,age=age, grade=grade)
        student.save()
        messages.success(request, "User Created Successfully.")
    return render (request, "create.html")