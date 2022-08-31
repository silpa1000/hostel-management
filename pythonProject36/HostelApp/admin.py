from django.contrib import admin

# Register your models here.
from HostelApp import models

admin.site.register(models.Login)
admin.site.register(models.Teacher)
admin.site.register(models.Student)
admin.site.register(models.Room)
admin.site.register(models.Food)
admin.site.register(models.Attendance)
admin.site.register(models.BookRoom)
admin.site.register(models.Complaint)
admin.site.register(models.Bill)




