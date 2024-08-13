from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import Student, Subject, User, Question, Assignment, StudentAnswer, StudentAnswerImage, AnswerRemark

class StudentSignUpForm(UserCreationForm):
    roll_no = forms.IntegerField(required=True, help_text='Enter your class roll number.',)
    semester = forms.IntegerField(required = True)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username','roll_no','semester','email','password1', 'password2',)




class TeacherSignUpForm(UserCreationForm):
    email = forms.EmailField()
    semester = forms.IntegerField(required = True)
    
    class Meta:
        model = User
        fields = ('username','email', 'semester', 'password1', 'password2',)


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('text', 'question_image', )


class AnswerRemarkForm(forms.ModelForm):
    Remarks = forms.CharField()

    class Meta:
        model = AnswerRemark
        fields = ('Remarks', )


class StudentAnswerForm(forms.ModelForm):
    text = forms.CharField(max_length=255)

    class Meta:
        model = StudentAnswer
        fields = ('text',)


class StudentAnswerImageForm(forms.ModelForm):
    answer_image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    answer_file = forms.FileField(
    widget=forms.ClearableFileInput(attrs={
        'multiple': True,
        'accept': 'application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document,application/vnd.ms-powerpoint,application/vnd.openxmlformats-officedocument.presentationml.presentation'
    }))

    class Meta:
        model = StudentAnswerImage
        fields = ('answer_image','answer_file',)