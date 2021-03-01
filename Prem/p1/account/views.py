from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth



# Create your views here.
def login(request):
        if request.method == "POST":
                username = request.POST["username"]
                password = request.POST["password"]

               
                User = auth.authenticate(username=username,password = password)
                if User is not None:
                        auth.login(request,User)
                        return redirect('/travello')
                else:
                        messages.info(request,"inavalid")
                        return redirect('login')
        else:
                return render (request,"login.html")

def register(request):
        
        

        if request.method == "POST":
                first_name = request.POST["first_name"]
                last_name = request.POST["last_name"]
                username = request.POST["user_name"]
                email = request.POST["email"]
                password = request.POST["password"]
                password1 = request.POST["password1"]

                if password == password1:
                        if User.objects.filter(username=username).exists():
                                messages.info(request,"username is taken")
                                return redirect ('register')
                        elif User.objects.filter(email = email).exists():
                                messages.info(request,"email is taken")
                                return redirect ('register')
                        else:
                                user = User.objects.create_user (username = username ,password = password, email = email, first_name = first_name, last_name = last_name)
                                user.save();
                                print("user created")
                                return redirect('login')
                      
                else:
                        messages.info(request,"password is not match")
                        return redirect ('register')
                return redirect('/travello')
        else:
                return render(request,"register.html")

def logout(request):
         auth.logout(request)
         return redirect('/travello')