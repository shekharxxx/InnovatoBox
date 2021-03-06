from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Video_up,Comment
# Create your views here.
def index(request):
    # registration page
    # signup logic
    if request.method == "POST":
        try:
            uname = request.POST['username']
            fname = request.POST['fname']
            lname = request.POST['lname']
            pass1 = request.POST['pass']
            pass2 = request.POST['rpass']
            mail1 = request.POST['email']
            
            if pass1 != pass2:
                messages.error(request, "PASSWORD DOES NOT MATCH ")
                return redirect('/inno_user/')
            
            user = User.objects.create_user(uname,mail1,pass1)
            user.first_name = fname
            user.last_name = lname
            user.save()
            messages.success(request,"user is registerd successfully")
            return redirect("/inno_user/login/")
        except:
            messages.warning(request,"username is already exist")
            return redirect("/inno_user/")
    else:
        return render(request, "inno_user/index.html") 

def signin(request):
    if request.method == 'POST':
        uname = request.POST.get('uname','')
        password = request.POST.get("password",'')
        
        luser = authenticate(username=uname, password=password)
        if luser is not None:
            login(request,luser)
            messages.success(request, " is successfully loged in")
            return redirect('/inno_user/dashbord/')
        else:
            messages.warning(request,"invalid user")
            return redirect('/inno_user/login/')
    else:
        return render(request,"inno_user/login.html")


def dashbord(request):
    v = Video_up.objects.all()
    c1 = Comment.objects.all()
    # list1 = []
    # list2 = []
    # for i in v:
    #     print(i.v_id)
    #     for j in c1:
    #         if i.v_id==j.cmt_vid:
    #             print("hi")
    l1 = v[::-1]
    return render(request,"inno_user/dashbord.html", { 'video' : l1, 'cmt' : c1})
    
def signout(request):
    logout(request)
    messages.success(request,"you are loged out")
    return redirect('/inno_user/')

def up_video(request):
    if request.method == "POST":
        v_title = request.POST.get('title', '')
        v_video = request.FILES['video']
        v_desc = request.POST.get('desc', '')
        v_user = request.POST.get('vname','')

        v_post = Video_up(v_title=v_title, v_file=v_video, v_desc=v_desc,v_user=v_user)
        v_post.save()
        messages.success(request, "'s Post uploaded successfully...")
        return redirect('/inno_user/up_video/')
        
    else:
        return render(request, "inno_user/up_video.html")

def cmt_upld(request):
    if request.method == "POST":
        c_user = request.POST.get('c_user', '')
        c_postid = request.POST.get('c_postid', '')
        cmt = request.POST.get('comment', '')

        com = Comment(cmt_user=c_user, cmt_vid=c_postid, cmt_msg=cmt)
        com.save()
        return redirect('/inno_user/dashbord/')