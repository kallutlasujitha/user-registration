from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import User


# Create your views here.
def SignUp(request):
    if request.method == 'POST':
        uname = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        
        if pass1!=pass2:
            return HttpResponse('Password not matched')
        
        elif User.objects.filter(u_name=uname).exists():
            return HttpResponse('username already exits!!!')
        else:
            my_user =User(u_name = uname,u_email = email,u_pass1=pass1,u_pass2 = pass2)
            my_user.save()
            

            return redirect('signup')
        
    return render(request,'signup.html')


def LogIn(request):
    if request.method == "POST":
        usernames = request.POST['username']
        pass1 = request.POST['pass']
 
        user =get_object_or_404(User,u_name = usernames)

        if user.u_pass1 == pass1:
            
            return redirect('home',user_id = user.id)
        
        else:
            
            return HttpResponse('Username and password does not exits!!!')
    
    
def Home(request,user_id):
    return render(request,'home.html',{'user_id':user_id})


def Delete(request,user_id):
    user = get_object_or_404(User,id=user_id)
    user.delete()
    return redirect('signup')


def LogOut(request):
    return redirect('signup')