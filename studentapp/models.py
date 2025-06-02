from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField(auto_now_add=True)
    





Course


id (AutoField)


name (CharField)


code (CharField, unique)


description (TextField)


Enrollment


id (AutoField)


student (ForeignKey to Student)
course (ForeignKey to Course)


enrollment_date (DateField)


Unique together on (student, course)


Assessment


id (AutoField)


course (ForeignKey to Course)


title (CharField)


total_marks (IntegerField)


due_date (DateField)


Grade


id (AutoField)


student (ForeignKey to Student)


assessment (ForeignKey to Assessment)


marks_obtained (IntegerField)


Validate: marks_obtained ≤ total_marks


