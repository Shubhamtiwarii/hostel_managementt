from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from hostel.models import *

# Register your models here.
def getFieldsModel(model):
    fields = [field.name for field in model._meta.get_fields() if field.many_to_many != True and field.one_to_many != True]
    return fields


class UserModel(admin.ModelAdmin):
    list_display = getFieldsModel(CustomUser)

class HostelModel(admin.ModelAdmin):
    list_display = getFieldsModel(Hostels)
    
# class RoomModel(admin.ModelAdmin):
#     #list_display = getFieldsModel(Room_types)
#     list_display=['id','HostelName','room_type']
#     def HostelName(self, instance):
#         return instance.hostel_id.hostel_name
    
    
class RoomNumModel(admin.ModelAdmin):
    #list_display = getFieldsModel(Room_nums)
    list_display=['id','HostelName','RoomType','room_num']
    def HostelName(self, instance):
        return instance.hostel_id.hostel_name
    def RoomType(self, instance):
        return instance.room_type


    


class AdminModel(admin.ModelAdmin):
    list_display = getFieldsModel(AdminHOD)

class StaffModel(admin.ModelAdmin):
    list_display = getFieldsModel(Staffs)

# class Room_book_model(admin.ModelAdmin):
#     list_display=['id','HostelName','RoomType','from_date','to_date']

#     def HostelName(self, instance):
#         return instance.room_num.hostel_id.hostel_name
#     def RoomType(self, instance):
#         return instance.room_num.room_type
    
class Room_book_model(admin.ModelAdmin):
    list_display=['id','Staff','hostel_name','room_number','room_type','from_date','to_date','status']

    def Staff(self,instance):
        return instance.staff.admin.id

admin.site.register(CustomUser,UserModel)
admin.site.register(Hostels,HostelModel)
# admin.site.register(Room_types,RoomModel)
admin.site.register(Room_nums,RoomNumModel)
admin.site.register(AdminHOD,AdminModel)
admin.site.register(Staffs,StaffModel)
admin.site.register(Room_book,Room_book_model)