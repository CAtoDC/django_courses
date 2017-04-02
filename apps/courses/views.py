from django.shortcuts import render, redirect
from models import Course

def index(request):
    courses = Course.objects.all()
    context = {
        "courses": courses
    }
    return render(request, 'courses/index.html', context)


def courses(request):
    # get info from form
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        # print (name, description)
        Course.objects.create(name=name, description=description)   # create object (row)
        courses = Course.objects.all()  # retrieve all objects
    context = {
        "courses": courses
    }
    return render(request, "courses/index.html", context)


def delete(request, id):
    # get info from form
    if request.method == 'POST':
        Course.objects.get(id=id).delete()
        return redirect ("/")
    else:
        # this is a GET
        course = Course.objects.get(id = id)
        context = {
            "course": course
        }
        return render(request, 'courses/delete_course.html', context)
