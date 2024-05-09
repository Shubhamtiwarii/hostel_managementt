from datetime import datetime
from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from hostel.models import *
from django.template.loader import render_to_string
from django.http import JsonResponse

def user_home(request):
    return render(request,"user_template/home_content.html")

def get_room(request):

    hostel=Hostels.objects.all()
    
    return render(request,"user_template/request_room.html",{'hostel':hostel})



def fetch_available_rooms(request):
    hostel_id = request.GET.get('hostel_id')
    if hostel_id:
        # Fetch available rooms based on hostel_id
        available_rooms = Room_nums.objects.filter(hostel_id=hostel_id)
        #room_numbers = [room.room_num for room in available_rooms]
        room_types=[room.room_type for room in available_rooms ]
        #room_numbers=[room.room_num for room in room_types]
        # Render HTML fragment for available rooms
        #rooms_html = render_to_string('user_template/request_room.html', {'available_rooms': available_rooms}
        # def check_room(room_numbers):
        #     if len(room_numbers) == 0:
        #         return 0
        #     else:
        #         return 1
        # if check_room(room_numbers):
        #     print("Room Is not Empty")
            
        # else:
        #     print("Emplty")
        #     #messages.error(request,"Room Is not Available in this hostel")
        #     return JsonResponse({'error': 'Room Is not Available in this hostel'}, status=400)
        #print(room_numbers)
        print(room_types)
        return JsonResponse({'room_types':room_types})

    return JsonResponse({'error': 'Hostel ID not provided'}, status=400)

def fetch_available_room_numbers(request):
    hostel_id = request.GET.get('hostel_id')
    room_type = request.GET.get('room_type')
    print(hostel_id,room_type)
    if hostel_id and room_type:
        available_rooms = Room_nums.objects.filter(hostel_id=hostel_id, room_type=room_type)
        room_numbers = [room.room_num for room in available_rooms]
        return JsonResponse({'room_numbers': room_numbers})
    return JsonResponse({'error': 'Hostel ID or room type not provided'}, status=400)

def request_room(request):
    '''
    if request.method=="POST":
        hostel_select=request.POST.get("hostel_select")
        hostel_name=Hostels.objects.get(id=hostel_select)
        hostel_name=hostel_name.hostel_name
        room_type=request.POST.get("room_type")
        room_number=request.POST.get("room_number")
        from_date=request.POST.get("from_date")
        to_date=request.POST.get("to_date")

        user=request.user
        #print(user)
        user=CustomUser.objects.get(id=user.id)
        #print(user.username)
        us=Staffs.objects.get(admin_id=user)
        #print(us.id)
        # s=Room_book.objects.filter(from_date__gte=from_date,to_date__lte=to_date,hostel_name=hostel_name,room_type=room_type,room_number=room_number)
        s=Room_book.objects.filter(hostel_name=hostel_name,room_type=room_type,room_number=room_number).all()
        print(s)
        for s in s:
            #if str(s.from_date)>=from_date and str(s.to_date)<=to_date:
            #if str(s.to_date)<=from_date:
           
            from_str=from_date
            date_object = datetime.strptime(from_str, '%Y-%m-%d').date()
            print(type(date_object))
            print(type(s.to_date))
            if date_object>s.to_date or date_object>s.from_date:
                s=Room_book(staff=us,hostel_name=hostel_name,room_type=room_type,room_number=room_number,from_date=from_date,to_date=to_date,status=0)
                #s.save()
                messages.success(request,"Request Is Succesfully Sent")
                return render(request,"user_template/request_room.html")
            else:
                messages.error(request,"Room Is already booked between days")
                return render(request,"user_template/request_room.html")
        print(s)
        

        print(hostel_name,room_type,room_number,from_date,to_date)
        #s=Room_book(staff=us,hostel_name=hostel_name,room_type=room_type,room_number=room_number,from_date=from_date,to_date=to_date,status=0)
        #s.save()
        #h=Room_nums.objects.filter(hostel_id=hostel_select,room_num=room_number,room_type=room_type)
        
        #for h in h:
        #    h.status=1
        #    h.save()
        #   print(h.id)
        messages.success(request,"Request Is Succesfully Sent")
        return render(request,"user_template/request_room.html")
    else:
        messages.error(request,"Failed to Sent Request")
        return render(request,"user_template/request_room.html")
     '''
    if request.method == "POST":
        hostel_select = request.POST.get("hostel_select")
        room_type = request.POST.get("room_type")
        room_number = request.POST.get("room_number")
        from_date = datetime.strptime(request.POST.get("from_date"), '%Y-%m-%d').date()
        to_date = datetime.strptime(request.POST.get("to_date"), '%Y-%m-%d').date()

        user_id = request.user.id
        try:
            user = CustomUser.objects.get(id=user_id)
            staff = Staffs.objects.get(admin_id=user)
        except (CustomUser.DoesNotExist, Staffs.DoesNotExist):
            messages.error(request, "Invalid user")
            return render(request, "user_template/request_room.html")

        try:
            hostel = Hostels.objects.get(id=hostel_select)
        except Hostels.DoesNotExist:
            messages.error(request, "Invalid hostel")
            return render(request, "user_template/request_room.html")

        conflicting_bookings = Room_book.objects.filter(
            hostel_name=hostel.hostel_name,
            room_type=room_type,
            room_number=room_number,
            to_date__gte=from_date,
            from_date__lte=to_date,
            status__in=[0,1],
        )
        

        if conflicting_bookings.exists():
            messages.error(request, "Room is already booked between selected dates")
            return redirect('get_room')
        else:
            new_booking = Room_book.objects.create(
                staff=staff,
                hostel_name=hostel.hostel_name,
                room_type=room_type,
                room_number=room_number,
                from_date=from_date,
                to_date=to_date,
                status=0
            )
            messages.success(request, "Request is successfully sent")

    return render(request, "user_template/request_room.html") 
def accmodation_history(request):
    user=request.user
    print("hlo",user.id)
    #room_history=Room_book.objects.all()
    st=Staffs.objects.get(admin=user.id)

    print(st.id)
    room_history=Room_book.objects.filter(staff=st.id)
    print(room_history)
    return render(request,"user_template/accmodation_history.html",{'room_history':room_history})