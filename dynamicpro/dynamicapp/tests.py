from django.test import TestCase
from .models import Student, Grade, Course, Teacher
from .views import index, getcourses, getgrade, getstudent, getteachers
from django.urls import reverse 
from django.contrib.auth.models import User
from .forms import studentForm


# Create your tests here.
class studentTypeTest(TestCase):
    def test_string(self):
        type=Student(stufname="kidane")
        self.assertEqual(str(type), type.stufname)
    
    def test_table(self):
        self.assertEqual(str(Student._meta.db_table), 'student')

class courseTypeTest(TestCase):
    def test_string(self):
        type=Course(courname="Python")
        self.assertEqual(str(type), type.courname)
    
    def test_table(self):
        self.assertEqual(str(Course._meta.db_table), 'course')

class indexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    

class getstudent(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('students'))
        self.assertEqual(response.status_code, 200)

class getteachers(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('teachers'))
        self.assertEqual(response.status_code, 200)


class coursedetails(TestCase):

    
    def setUp(self):
        
        self.course=Course.objects.create(courname='python', courcredit=5, courdescription='programming', courseprice=1200)

    def test_course_detail_sucess(self):
        response=self.client.get(reverse('coursedetails', args=(self.course.id,)))
        self.assertEqual(response.status_code, 200)


class studentformtest(TestCase):
    def test_studentform(self):
        data={
            'stufname': 'kidane',
            'stulname': 'Gidey',
            'stuphone': '0987654321',
            'studescription':'programming student'
        }
        form=studentForm(data=data)
        self.assertTrue(form.is_valid)

    def test_studentforminvalid(self):
        data={
            'stufname': '',
            'stulname': 'Gidey',
            'stuphone': '0987654321',
            'studescription':'programming student'
        }
        form=studentForm(data=data)
        self.assertFalse(form.is_valid())







    




