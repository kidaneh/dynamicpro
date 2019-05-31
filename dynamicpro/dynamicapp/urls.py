from django.urls import path
from . import views
urlpatterns=[
    path('', views.index, name='index'),
    path('getcourses/', views.getcourses, name='courses'),
    path('coursedetails/<int:id>', views.coursedetails, name='coursedetails'),
    path('getstudent/', views.getstudent, name='students'),
    path('getteachers/', views.getteachers, name='teachers'),
    path('getgrade/', views.getgrade, name='grades'),
    path('newstudent/', views.newstudent, name='newstudent'),
    path('newteacher/', views.newteacher, name='newteacher'),
    path('newcourse/', views.newcourse, name='newcourse'),
    path('newgrade/', views.newgrade, name='newgrade'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),





]