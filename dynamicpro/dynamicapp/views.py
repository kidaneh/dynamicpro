from django.shortcuts import render, get_object_or_404
from .models import Course, Student, Grade, Teacher
from .forms import studentForm, teacherForm, courseForm, gradeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


 
def index(request):
    return render(request, 'dynamicapp/index.html')

# Create your views here.

def getcourses(request):
    course_list=Course.objects.all()
    return render(request,'dynamicapp/courses.html', {'course_list': course_list})


def getstudent(request):
    student_list=Student.objects.all()
    return render(request,'dynamicapp/students.html', {'student_list': student_list})

def getteachers(request):
    teachers_list=Teacher.objects.all()
    return render(request,'dynamicapp/teachers.html', {'teachers_list': teachers_list})
    

def getgrade(request):
    grades_list=Grade.objects.all()
    return render(request,'dynamicapp/grades.html', {'grades_list': grades_list})
    

def coursedetails(request, id):
    coursedetail=get_object_or_404(Course, pk=id)
    context={
            'coursedetail': coursedetail,

    }  
    return render(request, 'dynamicapp/coursedetail.html', context=context)



def newstudent(request):
        form =studentForm
        if request.method=='POST':
                form=studentForm(request.POST)
                if form.is_valid():
                        post=form.save(commit=True)
                        post.save
                        form=studentForm()
        else:
                form=studentForm()
        return render (request, 'dynamicapp/newstudent.html',{'form': form})

def newcourse(request):
        form =courseForm
        if request.method=='POST':
                form=courseForm(request.POST)
                if form.is_valid():
                        post=form.save(commit=True)
                        post.save
                        form=courseForm()
        else:
                form=courseForm()
        return render (request, 'dynamicapp/newcourse.html',{'form': form})
        
@login_required
def newteacher(request):
        form =teacherForm
        if request.method=='POST':
                form=teacherForm(request.POST)
                if form.is_valid():
                        post=form.save(commit=True)
                        post.save
                        form=teacherForm()
        else:
                form=teacherForm()
        return render (request, 'dynamicapp/newteacher.html',{'form': form})


@login_required
def newgrade(request):
        form =gradeForm
        if request.method=='POST':
                form=gradeForm(request.POST)
                if form.is_valid():
                        post=form.save(commit=True)
                        post.save
                        form=gradeForm()
        else:
                form=gradeForm()
        return render (request, 'dynamicapp/newgrade.html',{'form': form})
     
def loginmessage(request):
        return render(request, 'dynamicapp/loginmessage.html')

def logoutmessage(request):
        return render(request, 'dynamicapp/logoutmessage.html')
