from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from hostel.EmailBackend import EmailBackEnd
from django.contrib import messages
# Create your views here.

def doLogin(request):
    if request.method !='POST':
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type=="1":
                return HttpResponseRedirect('/admin_home')
            else:
                return HttpResponseRedirect("/user_home")
                #return HttpResponse('staff home'+str(user.user_type))
            #return HttpResponse("Email:"+request.POST.get("email")+"Password:"+request.POST.get("password"))
        else:
            messages.error(request,"Invalid Login Credentials")
            return HttpResponseRedirect("/")
         
def showLoginPage(request):
    return render(request,"login_page.html")
def showDemoPage(request):
    return render(request,'demo.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")      
