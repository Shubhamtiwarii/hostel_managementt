"""
URL configuration for hostel_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from hostel import views,HodViews,UserViews
from hostel_management import settings

urlpatterns = [
    path('demo',views.showDemoPage),
    path('admin/', admin.site.urls),
    path('',views.showLoginPage),
    path('doLogin',views.doLogin),
    path('logout_user',views.logout_user),
    path('admin_home',HodViews.admin_home,name="admin_home"),
    path('add_hostel',HodViews.add_hostel),
    path('add_staff',HodViews.add_staff),
    #path('add_room_type',HodViews.add_room_type),
    path('add_room_nums',HodViews.add_room_nums),
    #path('add_room_type_save',HodViews.add_room_type_save),
    path('add_staff_save',HodViews.add_staff_save),
    path('add_hostel_save',HodViews.add_hostel_save),
    path('add_room_nums_save',HodViews.add_room_nums_save),
    path('manage_staff',HodViews.manage_staff),
    path('manage_hostel',HodViews.manage_hostel),
    path('manage_room',HodViews.manage_room_type),
    path('manage_room_nums',HodViews.manage_room_nums),
    path('user_home',UserViews.user_home,name="user_home"),
    path('get_room',UserViews.get_room,name="get_room"),
    path('fetch_available_rooms/', UserViews.fetch_available_rooms, name='fetch_available_rooms'),
    path('fetch_available_room_numbers/',UserViews.fetch_available_room_numbers, name='fetch_available_room_numbers'),
    path('request_room',UserViews.request_room),
    path('accmodation_history',UserViews.accmodation_history),
    path('accmodation_approval',HodViews.accmodation_approval,name='accmodation_approval'),
    path('accmodation_approve/<int:id>',HodViews.accmodation_approve,name="accmodation_approve"),
    path('accmodation_reject/<int:id>',HodViews.accmodation_reject,name="accmodation_reject"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
