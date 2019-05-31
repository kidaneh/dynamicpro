from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
    stufname=models.CharField(max_length=255)
    stulname=models.CharField(max_length=255)
    studentphone=models.CharField(max_length=10)
    studescription=models.TextField(null=True, blank=True)   

    def __str__(self):
        return self.stufname

    class Meta:
        db_table='student'
        verbose_name_plural='students'

class Course(models.Model):
    courname=models.CharField(max_length=255)
    courcredit=models.SmallIntegerField()
    courseprice=models.DecimalField(max_digits=10, decimal_places=2)
    courdescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.courname

    class Meta:
        db_table='course'
        verbose_name_plural='courses'

class Grade(models.Model):
    studentid=models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    courseid=models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    user=models.ManyToManyField(User)
    result=models.CharField(max_length=1)

    def __str__(self):
        return str(self.studentid)

    class Meta:
        db_table='grade'
        verbose_name_plural='grades'


class Teacher(models.Model):
    teafname=models.CharField(max_length=255)
    tealname=models.CharField(max_length=255)
    teatphone=models.CharField(max_length=10)
    teadescription=models.TextField(null=True, blank=True)
    

    def __str__(self):
        return self.teafname

    class Meta:
        db_table='teacher'
        verbose_name_plural='teachers'







