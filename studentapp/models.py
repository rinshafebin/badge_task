from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name



class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField(unique=True)
    description = models.TextField()
    
    def __str__(self):
        return self.name
 
   
class Enrollment(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    
    class Meta:
        unique_together = ('student','course')
        
    def __str__(self):
        return f'{self.student}'



class Assessment(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    total_marks = models.IntegerField()
    due_date = models.DateField()
    
    def __str__(self):
        return self.title



class Grade(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment,on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()
    
    def __str__(self):
        return f'{self.student} - {self.marks_obtained}'
    