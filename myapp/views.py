from django.shortcuts import render,redirect
from .forms import userform,updateform
from .models import userdata
from django.contrib.auth import logout
from django.core.mail import send_mail

# Create your views here.
def home(request):
    if request.method == "POST":
        user = userform(request.POST)
        if user.is_valid():
            user.save()
            
            sub = "Welcome"
            msg = "Dear User!\nYour Account has been Created With Agrovia Fields\nWelcome To Agrovia family\nEnjoy The Service Check Fruits\nChoose The Fruit Contact on\nmatinaibani8@gmail.com | +919510695745\nThank You!"
            fr_mail = "ptestmail22@gmail.com"
            to_mail = [request.POST["email"]]

            #This is For Checking Email....
            # em = request.POST["email"]
            # print("This is Email:",em)
            
            send_mail(subject=sub,message=msg,from_email=fr_mail,recipient_list=to_mail)
            print("Signup Successfull!")
            return redirect("index")
    return render(request,"signup.html")

def login(request):
    if request.method=="POST":
        unm = request.POST["username"]
        pas = request.POST["password"]

        user= userdata.objects.filter(email=unm,password=pas)
        uid = userdata.objects.get(email=unm)
        if user:
            request.session["user"] = unm
            request.session["uid"] = uid.id
            print("Login Successfull!")
            return redirect("index")
        else:
            print("Error!")
    else:
        return render(request,"login.html")

def userlogout(request):
    logout(request)
    return redirect("/")

def updateprofile(request):
    user = request.session.get("user")
    uid = request.session.get("uid")
    cid = userdata.objects.get(id=uid)
    if request.method == "POST":
        user = updateform(request.POST)
        if user.is_valid():
            update = updateform(request.POST,instance=cid)
            update.save()  
            print("Updated Profile!")
            return redirect("index")
        else:
            print(update.errors)
    return render(request,"updateprofile.html",{'stid':user,"uid":userdata.objects.get(id=uid)})


def index(request):
    user = request.session.get("user")
    return render(request,"index.html",{"cuser":user})

def about(request):
    user = request.session.get("user")
    return render(request,"about.html",{"cuser":user})

def service(request):
    user = request.session.get("user")
    return render(request,"service.html",{"cuser":user})

def blog(request):
    user = request.session.get("user")
    return render(request,"blog.html",{"cuser":user})

def feature(request):
    user = request.session.get("user")
    return render(request,"feature.html",{"cuser":user})

def team(request):
    user = request.session.get("user")
    return render(request,"team.html",{"cuser":user})

def testimonial(request):
    user = request.session.get("user")
    return render(request,"testimonial.html",{"cuser":user})

def error(request):
    user = request.session.get("user")
    return render(request,"404.html",{"cuser":user})

def contact(request):
    user = request.session.get("user")
    return render(request,"contact.html",{"cuser":user})