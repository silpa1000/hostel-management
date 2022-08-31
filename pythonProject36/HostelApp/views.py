from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import datetime
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
from django.urls import reverse

from HostelApp.forms import LoginForm,TeacherForm,StudentForm,RoomForm,FoodForm,AddAttendanceForm,BookRoomForm,ComplaintForm,BillForm,PaymentForm

from HostelApp.models import Login,Teacher,Student,Room,Food,Attendance,BookRoom,Complaint,Bill,PaymentMode

def index(request):
    return render(request,'index.html')
def signin(request):
    if request.method == 'POST':
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('admin_home')
            elif user.is_student:
                return redirect('student_home')
            elif user.is_teacher:
                return redirect('teacher_home')
        else:
            messages.info(request,'invalid credentials')
    return render(request,'login.html')
def admin_home(request):
    return render(request,'Admin/admin_home.html')
def teacher_register(request):
    login_form=LoginForm()
    teacher_form=TeacherForm()
    if request.method=='POST':
        login_form=LoginForm(request.POST)
        teacher_form=TeacherForm(request.POST,request.FILES)
        if login_form.is_valid() and teacher_form.is_valid():
            user=login_form.save(commit=False)
            user.is_teacher=True
            user.save()
            s=teacher_form.save(commit=False)
            s.user=user
            s.save()
            messages.info(request,'teacher registered successfully')
            return redirect('teacher_view')
    return render(request,'Admin/teacher_register.html',{'login_form':login_form,'teacher_form':teacher_form})

def teacher_view(request):
    st=Teacher.objects.all()
    return render(request,'Admin/teacher_view.html',{'st':st})
def teacher_update(request,id):
    st=Teacher.objects.get(id=id)
    s=Login.objects.get(teacher=st)
    if request.method=='POST':
        form=TeacherForm(request.POST or None,instance=st)
        login_form=LoginForm(request.POST or None,instance=s)
        if form.is_valid() and login_form.is_valid():
            form.save()
            login_form.save()
            messages.info(request,'teacher updated successfully')
            return redirect('teacher_view')
    else:
            form=TeacherForm(instance=st)
            login_form=LoginForm(instance=s)
    return render(request,'Admin/teacher_update.html',{'form':form,'login_form':login_form})
def teacher_delete(request,id):
    st=Teacher.objects.get(id=id)
    s=Login.objects.get(teacher=st)
    if request.method=='POST':
        s.delete()
        messages.info(request, 'teacher deleted successfully')
        return redirect('teacher_view')
    else:
        return redirect('teacher_view')
def logout(request):
    return redirect('signin')
def student_register(request):
    login_form=LoginForm()
    student_form=TeacherForm()
    if request.method=='POST':
        login_form=LoginForm(request.POST)
        student_form=StudentForm(request.POST,request.FILES)
        if login_form.is_valid() and student_form.is_valid():
            user=login_form.save(commit=False)
            user.is_student=True
            user.save()
            s=student_form.save(commit=False)
            s.user=user
            s.save()
            messages.info(request,'student registered successfully')
            return redirect('student_view')
    return render(request,'Admin/student_register.html',{'login_form':login_form,'student_form':student_form})
def student_view(request):
    sd=Student.objects.all()
    return render(request,'Admin/student_view.html',{'sd':sd})
def student_update(request,id):
    sd=Student.objects.get(id=id)
    s=Login.objects.get(student=sd)
    if request.method=='POST':
        form=StudentForm(request.POST or None,instance=sd)
        login_form=LoginForm(request.POST or None,instance=s)
        if form.is_valid() and login_form.is_valid():
            form.save()
            login_form.save()
            messages.info(request,'student updated successfully')
            return redirect('student_view')
    else:
            form=StudentForm(instance=sd)
            login_form=LoginForm(instance=s)
    return render(request,'Admin/student_update.html',{'form':form,'login_form':login_form})
def student_delete(request,id):
    sd=Student.objects.get(id=id)
    s=Login.objects.get(student=sd)
    if request.method=='POST':
        s.delete()
        messages.info(request, 'student deleted successfully')
        return redirect('student_view')
    else:
        return redirect('student_view')
def Room_Add(request):
    form=RoomForm()
    if request.method=='POST':
        form=RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Room_View')
    return render(request,'Admin/Room_Add.html',{'form':form})
def Room_View(request):
    rm = Room.objects.all()
    return render(request,'Admin/Room_View.html',{'rm':rm})
def Room_Update(request,id):
    rm=Room.objects.get(id=id)
    if request.method=='POST':
        form=RoomForm(request.POST or None,instance=rm)
        if form.is_valid():
           form.save()
           messages.info(request,'Room updated successfully')
           return redirect('Room_View')
    else:
        form=RoomForm(instance=rm)
    return render(request,'Admin/Room_Update.html',{'form':form})
def Room_Delete(request,id):
    rm=Room.objects.get(id=id)
    if request.method=='POST':
        rm.delete()
        return redirect('Room_View')
    else:
         return redirect('Room_View')
def student_home(request):
    return render(request,'Student/student_home.html')
def Food_Add(request):
    form=FoodForm()
    if request.method=='POST':
        form=FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Food_View')
    return render(request,'Admin/Food_Add.html',{'form':form})
def Food_View(request):
    fd = Food.objects.all()
    return render(request,'Admin/Food_View.html',{'fd':fd})
def Food_Update(request,id):
    fd=Food.objects.get(id=id)
    if request.method=='POST':
        form=FoodForm(request.POST or None,instance=fd)
        if form.is_valid():
           form.save()
           messages.info(request,'Food updated successfully')
           return redirect('Food_View')
    else:
        form=FoodForm(instance=fd)
    return render(request,'Admin/Food_Update.html',{'form':form})
def Food_Delete(request,id):
    fd=Food.objects.get(id=id)
    if request.method=='POST':
        fd.delete()
        return redirect('Food_View')
    else:
         return redirect('Food_View')
def stdroom_View(request):
    st=Room.objects.all()
    return render(request,'Student/View_Room.html',{'st':st})
def stdfood_View(request):
    sd=Food.objects.all()
    return render(request,'Student/View_Food.html',{'sd':sd})
def teacher_home(request):
    return render(request,'Teacher/teacher_home.html')
def teacherroom_View(request):
    tr=Room.objects.all()
    return render(request,'Teacher/trView_Room.html',{'tr':tr})
def teacherfood_View(request):
    td=Food.objects.all()
    return render(request,'Teacher/trView_Food.html',{'td':td})
# def approve_student(request,id):
#     student=Student.objects.get(user_id=id)
#     student.approval_status=True
#     student.save()
#     messages.info(request,'student approved successfully')
#     return HttpResponseRedirect(reverse('View_std_reg'))
# def reject_student(request,id):
#     student=Student.objects.get(user_id=id)
#     if request.method=='POST':
#         student.approval_status=False
#         student.save()
#         messages.info(request, 'student rejected successfully')
#         return redirect('student_view')
#     return render(request,'Admin/reject_student.html')
def studentprofile(request):
    u=request.user
    profile=Student.objects.filter(user_id=u)
    return render(request,'Student/studentprofile.html',{'profile':profile})

def add_attendance(request):
    student=Student.objects.all()
    return render(request,'Admin/add_attendance.html',{'student':student})
now=datetime.datetime.now()
def mark_attendance(request,id):
    user=Student.objects.get(id=id)
    att=Attendance.objects.filter(student=user,date=datetime.date.today())
    if att.exists():
        messages.info(request,'todays attendance already marked')
        return redirect('add_attendance')
    else:
        if request.method=='POST':
            attndc=request.POST.get('attendance')
            Attendance(student=user,date=datetime.date.today(),attendance=attndc,time=now.time()).save()
            messages.info(request,"Attendance added successfully")
            return redirect('add_attendance')
        return render(request,'Admin/mark_attendance.html')
def view_attendance(request):
    value_list=Attendance.objects.values_list('date',flat=True).distinct()
    attendance={}
    for value in value_list:
        attendance[value]=Attendance.objects.filter(date=value)
    return render(request,'Admin/view_attendance.html',{'attendance':attendance})
def day_attendance(request,date):
    attendance=Attendance.objects.filter(date=date)
    context={
        'attendance':attendance,
        'date':date
    }
    return render(request,'Admin/day_attendance.html',context)
def teacherprofile(request):
    u=request.user
    profile=Teacher.objects.filter(user_id=u)
    return render(request,'Teacher/teacherprofile.html',{'profile':profile})
def std_viewAtt(request):
    at=Attendance.objects.all()
    return render(request,'Student/std_viewAtt.html',{'at':at})
def att_view(request):
    at=Attendance.objects.all()
    return render(request,'Teacher/view_stdAtt.html',{'at':at})
def book_room(request):
    form=BookRoomForm()
    if request.method=='POST':
        form=BookRoomForm(request.POST)
        if form.is_valid():
            book=form.save(commit=False)
            book.student=Student.objects.get(user=request.user)
            book.date_joining=form.cleaned_data.get('date_joining')
            book.booking_date=form.cleaned_data.get('booking_data')
            book.booked_by=request.user
            student_qs=BookRoomForm.objects.filter(student=Student.objects.get(user=request.user))
            if student_qs.exists():
                messages.info(request,'You have already booked room')
            else:
                book.save()
                messages.info(request,'successfully booked room')
                return redirect('booking_status')
    return render(request,'Student/book_room.html',{'forms':form})
def booking_status(request):
    student=Student.objects.get(user=request.user)
    status=BookRoomForm.objects.filter(student=student)
    return render(request,'Student/booking_status.html',{'status':status})
def cancel_booking(request,id):
    book=BookRoomForm.objects.filter(pk=id)
    if request.method == 'POST':
        book.delete()
        messages.info(request,'Your booking has been cancelled')
        return redirect('booking_status')
    return render(request,'student/cancel_booking.html')
def bookings(request):
    book=BookRoomForm.objects.all()
    for i in book:
        i.seen=True
        i.save()
    request.session['booking']=0
    return render(request,'admin/bookings.html',{'books':book})
def confirm_booking(request,id):
    details_qs=Room.objects.all()
    if details_qs.exist():
        book=BookRoomForm.objects.get(id=id)
        book.status=1
        book.save()
        hstl=Room.objects.all().last()
        occupied=hstl.occupied
        hstl.occupied=int(occupied)-1
        hstl.save()
        messages.info(request,'Room booking confirmed')
        return redirect('bookings')
    else:
        messages.info(request,'Please update hostel details')
        return HttpResponseRedirect(reverse('bookings'))
def reject_booking(request,id):
    book=BookRoomForm.objects.get(id=id)
    if request.method=='POST':
        book.status=2
        book.save()
        messages.info(request,'Room booking rejected')
        return redirect('booking')
    return render(request,'Admin/reject_booking.html')

def complaintAdd(request):
    form=ComplaintForm()
    u=request.user
    if request.method=='POST':
        form=ComplaintForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
            messages.info(request,'complaint registered successfully')
            return redirect('ComplaintView')
    else:
        form=ComplaintForm()
    return render(request,'Student/complaint_Add.html',{'form':form})
def ComplaintView(request):
    cp=Complaint.objects.all()
    return render(request,'Student/complaint_view.html',{'cp':cp})
def admincmpView(request):
    pl = Complaint.objects.all()
    return render(request, 'Admin/admincmpView.html', {'pl':pl})
@login_required(login_url='signin')
def cmpReply(request,id):
    complaint=Complaint.objects.get(id=id)
    if request.method=='POST':
        c=request.POST.get('reply')
        complaint.reply=c
        complaint.save()
        messages.info(request,'reply send for complaint')
        return redirect('admincmpView')
    return render(request,'Admin/cmpReply.html',{'complaint':complaint})
def cmpreplyView(request):
    rv= Complaint.objects.all()
    return render(request, 'Student/cmpreplyView.html', {'rv':rv})
def bill_add(request):
    bill_form=BillForm()
    if request.method=='POST':
        bill_form=BillForm(request.POST)
        if bill_form.is_valid():
            bill_form.save()
            return redirect('bill_view')
    return render(request,'Admin/bill_add.html',{'bill_form':bill_form})
def bill_view(request):
    bill=Bill.objects.all()
    return render(request,'Admin/bill_view.html',{'bill':bill})
def bill_student_view(request):
    u=request.user
    bill=Student.objects.get(user=u)
    bill_view=Bill.objects.filter()
    return render(request,'Student/bill_student_view.html',{'bill_view':bill_view})
def pay_bill(request):
    bi=Bill.objects.get(id=id)
    form=PaymentForm()
    if request.method=='POST':
        card=request.POST.get('card')
        cvv=request.POST.get('cvv')
        date=request.POST.get('exp_date')
        PaymentMode(card_no=card,card_cvv=cvv,expiry_date=date).save()
        bi.status=1
        bi.save()
        messages.info(request,'Bill paid successfully')
        return redirect('bill_history')
    return render(request,'Student/pay_bill.html',{'form':form})
def bill_history(request):
    pb=Bill.objects.all()
    return render(request,'Student/bill_history.html',{'pb':pb})



