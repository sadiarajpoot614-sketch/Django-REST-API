from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer

from django.shortcuts import render, redirect, get_object_or_404


# API CRUD
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



# Website CRUD Dashboard

def student_list(request):
    students = Student.objects.all()
    return render(request, "students.html", {"students": students})


def add_student(request):
    if request.method == "POST":
        name = request.POST["name"]
        age = request.POST["age"]
        course = request.POST["course"]

        Student.objects.create(
            name=name,
            age=age,
            course=course
        )

        return redirect("students")

    return render(request, "add_student.html")



def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.name = request.POST["name"]
        student.age = request.POST["age"]
        student.course = request.POST["course"]

        student.save()

        return redirect("students")

    return render(request, "edit_student.html", {"student": student})



def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()

    return redirect("students")