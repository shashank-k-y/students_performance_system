from django.contrib import admin

from student_accounts.models import Student, Score, Subject

admin.site.register(Student)
admin.site.register(Score)
admin.site.register(Subject)
