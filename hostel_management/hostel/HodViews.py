from datetime import datetime
from django.conf import settings
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
#from hostel.models import CustomUser,Staffs,Room_nums,Hostels,Room_book
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from django.db import connection
cursor=connection.cursor()



def admin_home(request):
    return render(request,"hod_template/home_content.html")

def add_hostel(request):
    return render(request,"hod_template/add_hostel_template.html")

# def add_room_type(request):
#     pass
#     # hostels=Hostels.objects.all()
#     # return render(request,"hod_template/add_room_type_template.html",{"hostels":hostels})

# def add_room_type_save(request):
#     pass
#     # if request.method!='POST':
#     #     return HttpResponse("Method not allowed")
#     # else:
#     #     room_type=request.POST.get("room_type")
#     #     hostel_id=request.POST.get("hostel")
#     #     hostel=Hostels.objects.get(id=hostel_id)
#     #     try:
#     #         room=Room_types(room_type=room_type,hostel_id=hostel)
#     #         room.save()
#     #         messages.success(request,"Successfully Added Room Type")
#     #         return HttpResponseRedirect("/add_room_type")
#     #     except:
#     #         messages.error(request,"Failed to Add Room Type")
#     #         return HttpResponseRedirect("/add_room_type")

def add_room_nums(request):
    hostels=Hostels.objects.all()
    # room_types=Room_types.objects.all()
    return render(request,"hod_template/add_room_nums_template.html",{"hostels":hostels})

def add_room_nums_save(request):
    if request.method!='POST':
        return HttpResponse("Method not allowed")
    else:
        room_num=request.POST.get("room_num")
        room_type=request.POST.get("room_type")
        # room=Room_types.objects.get(id=room_id)
        hostel_id=request.POST.get("hostel")
        hostel=Hostels.objects.get(id=hostel_id)
        try:
            room=Room_nums(room_num=room_num,room_type=room_type,hostel_id=hostel)
            room.save()
            messages.success(request,"Successfully Added Room Number")
            return HttpResponseRedirect("/add_room_nums")
        except:
            messages.error(request,"Failed to Add Room Number")
            return HttpResponseRedirect("/add_room_nums")


    




def add_staff(request):
    return render(request,"hod_template/add_staff_template.html")

def add_staff_save(request):
    if request.method!='POST':
        return HttpResponse('Method Not Allowed')
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        address=request.POST.get("address")
        designation=request.POST.get("designation")
        sex=request.POST.get("sex")
        remarks=request.POST.get("remarks")
        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=2)
            user.staffs.address=address
            user.staffs.designation=designation
            user.staffs.gender=sex
            user.staffs.remarks=remarks
            user.save()
            messages.success(request,"Successfully Added Student")
            return HttpResponseRedirect("/add_staff")
        except:
            messages.error(request,"Failed to Add Student")
            return HttpResponseRedirect("/add_staff")
        
def add_hostel_save(request):
    if request.method!='POST':
        return HttpResponse("Method not allowed")
    else:
        hostel=request.POST.get("hostel")
        try:
            hostel_model=Hostels(hostel_name=hostel)
            hostel_model.save()
            messages.success(request,"Successfully Added Hostel")
            return HttpResponseRedirect("/add_hostel")
        except:
            messages.error(request,"Failed to Add Hostel")
            return HttpResponseRedirect("/add_hostel")  




def manage_staff(request):
    staffs=Staffs.objects.all()
    return render(request,"hod_template/manage_staff_template.html",{"staffs":staffs})


def manage_hostel(request):
    #hostels=Hostels.objects.all()
    cursor.execute('exec hostel')
    hostels=cursor.fetchall()
    print("hlo",hostels)
    return render(request,"hod_template/manage_hostel_template.html",{"hostels":hostels})

def manage_room_type(request):
    pass
    #rooms=Room_types.objects.all()
    # return render(request,"hod_template/manage_room_type_template.html",{"rooms":rooms})


def manage_room_nums(request):
    
    rooms=Room_nums.objects.all()
   # room_type=Room_types.objects.all()
    return render(request,"hod_template/manage_room_nums_template.html",{"rooms":rooms})

def accmodation_approval(request):
    room_approval=Room_book.objects.all().order_by('-id')
    user=request.user
    admin=AdminHOD.objects.get(admin=user)
    #app_id=Room_book.objects.get(id=)
    #rint(admin.id)
    #print(user)
    return render(request,"hod_template/accmodation_approval.html",{'room_approval':room_approval})

def accmodation_approve(request,id):
    accom=Room_book.objects.get(id=id)
    accom.status=1
    accom.save()
    subject = 'Hostel Accmodation'
    message = f'Hi {accom.staff.admin.first_name}, Your accmodation is approved< from {accom.from_date} date  to till {accom.to_date} date Thanks and Regards.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [accom.staff.admin.email, ]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('accmodation_approval')

def accmodation_reject(request,id):
    accom=Room_book.objects.get(id=id)
    accom.status=2
    accom.save()
    #print(accom.id,accom.room_number,accom.room_type,accom.hostel_name)
    # hostel_id=Hostels.objects.filter(hostel_name=accom.hostel_name)
    # for h in hostel_id:
    #     print(h.id)
    # s=Room_nums.objects.filter(hostel_id=h.id,room_num=accom.room_number,room_type=accom.room_type)
    # for s in s:
    #     s.status=0
    #     #print(s)
    #     s.save()
    
    return redirect('accmodation_approval')

