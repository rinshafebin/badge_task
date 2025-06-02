from django.contrib import admin
from studentapp.models import Student,Course,Assessment,Enrollment,Grade
# Register your models here.

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Assessment)
admin.site.register(Enrollment)
admin.site.register(Grade)

