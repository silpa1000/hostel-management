from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.core.validators import MinLengthValidator

# Create your models here.
class Login(AbstractUser):
    is_staff=models.BooleanField(default=False)
    is_teacher=models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)
class Teacher(models.Model):
    user=models.ForeignKey(Login,on_delete=models.CASCADE,related_name='teacher')
    Name=models.CharField(max_length=50)
    Age=models.IntegerField()
    Address=models.CharField(max_length=750)
    Branch=models.CharField(max_length=400)
    Email=models.EmailField(max_length=50)
    Contact_No=models.CharField(max_length=50)
    photo = models.ImageField(upload_to='uploads')
    def __str__(self):
        return self.name
class Student(models.Model):
    user=models.ForeignKey(Login,on_delete=models.CASCADE,related_name='student')
    Name=models.CharField(max_length=50)
    Age=models.IntegerField()
    Enrollment_no=models.CharField(max_length=10,unique=True,null=True)
    Branch=models.CharField(max_length=400)
    dob=models.DateField(max_length=10,help_text="format:YYYY-MM-DD",null=True)
    Contact_No=models.CharField(max_length=50)
    # approval_status=models.BooleanField(default=0)
    photo=models.ImageField(upload_to='uploads/')
    # def __str__(self):
    #     return self.name
class Room(models.Model):
    room_choice = [('S', 'Single Occupancy'), ('D', 'Double Occupancy')]
    no = models.CharField(validators=[MinLengthValidator(2)], max_length=5, unique=True)
    max_persons = models.IntegerField(default=2)
    room_type = models.CharField(choices=room_choice, max_length=1, default=None)
    price = models.IntegerField(default=500)

    def __str__(self):
        return 'Room no: %s price: %s' % (str(self.no), str(self.price))
        return self.name
class Food(models.Model):
    Breakfast=models.CharField(max_length=50)
    Lunch=models.CharField(max_length=50)
    Dinner=models.CharField(max_length=50)
class Attendance(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='attendance')
    attendance=models.CharField(max_length=100)
    date = models.DateField()
    time=models.TimeField()
class BookRoom(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    date_joining=models.DateField()
    booking_date=models.DateField(auto_now_add=True)
    status=models.IntegerField(default=0)
    # booked_by=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    seen=models.BooleanField(default=False)
    def __str__(self):
        return self.name
class Complaint(models.Model):
    name=models.CharField(max_length=300)
    subject=models.CharField(max_length=250)
    description=models.CharField(max_length=550)
    date=models.DateField()
    reply=models.TextField(null=True,blank=True)
class Bill(models.Model):
    name=models.CharField(max_length=300)
    bill_date=models.DateTimeField(auto_now_add=True)
    amount=models.IntegerField()
    paid_on=models.DateField(auto_now=True)
    status=models.IntegerField(default=0)

    def __str__(self):
        return self.name
class PaymentMode(models.Model):
    name = models.CharField(max_length=300)
    card_no=models.CharField(max_length=20,null=True)
    card_cvv=models.CharField(max_length=10,null=True)
    expiry_date=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name