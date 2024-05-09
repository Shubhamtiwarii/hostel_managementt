from datetime import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class CustomUser(AbstractUser):
    user_type_data=((1,"HOD"),(2,"Staff"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)

class AdminHOD(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Staffs(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    gender=models.CharField(max_length=255)
    designation=models.CharField(max_length=255)
    address=models.TextField()
    remarks=models.TextField(max_length=250)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Hostels(models.Model):
    id=models.AutoField(primary_key=True)
    hostel_name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

# class Room_types(models.Model):
#     id=models.AutoField(primary_key=True)
#     hostel_id=models.ForeignKey(Hostels,on_delete=models.CASCADE)
#     room_type=models.CharField(max_length=255)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now_add=True)
#     objects=models.Manager()

class Room_nums(models.Model):
    id=models.AutoField(primary_key=True)
    hostel_id=models.ForeignKey(Hostels,on_delete=models.CASCADE)
    room_type=models.CharField(max_length=100)
    room_num=models.IntegerField()
    #status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

    # def __str__(self):
    #     return self.hostel_id.hostel_name


class Room_book(models.Model):
    #room_num=models.ForeignKey(Room_nums,on_delete=models.CASCADE)
    staff=models.ForeignKey(Staffs,on_delete=models.CASCADE)
    hostel_name=models.CharField(max_length=100)
    room_type=models.CharField(max_length=100)
    room_number=models.IntegerField()
    from_date=models.DateField()
    to_date=models.DateField()
    status=models.IntegerField() 
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type==2:
            Staffs.objects.create(admin=instance,address="")

@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.adminhod.save()
    if instance.user_type==2:
        instance.staffs.save()


