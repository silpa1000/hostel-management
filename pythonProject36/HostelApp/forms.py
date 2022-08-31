import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from HostelApp.models import Login,Teacher,Student,Room,Food,Attendance,BookRoom,Complaint,Bill,PaymentMode

def phone_number_validator(value):
    if not re.compile(r'^[7-9]\d{9}$').match(value):
        raise ValidationError('This is Not a Valid Phone Number')
class DateInput(forms.DateInput):
    input_type = 'date'



class LoginForm(UserCreationForm):
    username=forms.CharField()
    password1=forms.CharField(label='password',widget=forms.PasswordInput)
    password2=forms.CharField(label='confirm password',widget=forms.PasswordInput)
    class Meta:
        model=Login
        fields=('username','password1','password2')
class TeacherForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields=('Name','Age','Address','Branch','Email','Contact_No','photo')
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields = ('Name', 'Age', 'Enrollment_no', 'Branch', 'dob', 'Contact_No', 'photo')
class RoomForm(forms.ModelForm):
    class Meta:
        model=Room
        fields='__all__'
class FoodForm(forms.ModelForm):
    class Meta:
        model=Food
        exclude=('user',)
class AddAttendanceForm(forms.ModelForm):
    class Meta:
        model=Attendance
        fields=('student','attendance')
class BookRoomForm(forms.ModelForm):
    class Meta:
        model=BookRoom
        fields='__all__'
class ComplaintForm(forms.ModelForm):
    date=forms.DateField(widget=DateInput)
    class Meta:
        model=Complaint
        fields=('name','subject','description','date')
class BillForm(forms.ModelForm):
    class Meta:
        model=Bill
        fields=('name','amount')
class PaymentForm(forms.ModelForm):
    card_no=forms.CharField(validators=[RegexValidator(regex='^.{16}$',message='Please enter a valid card no.')])
    card_cvv=forms.CharField(widget=forms.PasswordInput,validators=[RegexValidator(regex='^.{3}$',message='Please enter a valid cvv')])
    expiry_date=forms.DateField(widget=DateInput(attrs={'id':'example-month-input'}))
    class Meta:
        model=PaymentMode
        fields=('card_no','card_cvv','expiry_date')