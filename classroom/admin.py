from django.contrib import admin
from .models import User, Subject, Question, Assignment,Student, StudentAnswerImage, StudentAnswer, Teacher

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Question)
# admin.site.register(Assignment)

# admin.site.register(StudentAnswer)
# admin.site.register(StudentAnswerImage)