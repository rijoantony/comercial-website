from django.shortcuts import render,redirect,HttpResponse
from app1.models import useraccount,addrest,viewrest,addmenu,addfood,addoffer,addfeedback
# for authentication
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

# Create your views here.
# go to pages from index
def indexf(request):
    return render(request,"index.html")
def usercreatef(request):
    return render(request,"usercreate.html")
def userlogf(request):
    return render(request,"userlogin.html")
def admincreatef(request):
    return render(request,"admincreate.html")
def adminloginf(request):
    return render(request,"adminlogin.html")
def restpublicf(request):
    return render(request,"restpublic.html")
# to view

def viewmenuindexf(request):
     O1=addmenu.objects.all()
     return render(request,"viewmenuindex.html",{'x':O1})
def viewoffersindexf(request):
    O1=addoffer.objects.all()
    return render(request,"viewoffersindex.html",{'x':O1})
def viewrestindexf(request):
    O1=addrest.objects.all()
    return render(request,"viewrestindex.html",{'x':O1})



# go to pages from admin1 to add
def addrestf(request):
    return render(request,"addrest.html")
def addoffersf(request):
    return render(request,"addoffers.html")
# to view
def viewrestf(request):
    O1=addrest.objects.all()
    return render(request,"viewrest.html",{'x':O1})
def viewmenuadminf(request):
    O1=addmenu.objects.all()
    return render(request,"viewmenuadmin.html",{'x':O1})
def viewfoodadminf(request):
    O1=addfood.objects.all()
    return render(request,"viewfoodadmin.html",{'x':O1})
def viewoffersadminf(request):
    O1=addoffer.objects.all()
    return render(request,"viewoffersadmin.html",{'x':O1})
def viewfeedbackadminf(request):
    O1=addfeedback.objects.all()
    return render(request,"viewfeedbackadmin.html",{'x':O1})

def Viewprofilef(request):
    O1=User.objects.get(is_superuser=1)
    print("test1",O1)
    return render(request,"updateprofile.html",{'x':O1})

# to show update table
def viewupdaterestf(request):
    O1=addrest.objects.all()
    return render(request,"viewupdaterest.html",{'x':O1})

def updateoffersf(request):
    O1=addoffer.objects.all()
    return render(request,"viewupdateoffer.html",{'x':O1})

def updatemenuadminf(request):
    O1=addmenu.objects.all()
    return render(request,"viewupdatemenuadmin.html",{'x':O1})

def updatefoodadminf(request):
    O1=addfood.objects.all()
    return render(request,"viewupdatefoodadmin.html",{'x':O1})

def updateprofilef(request):
    O1=User.objects.get(is_superuser=1)
    return render(request,"viewupdateprofile.html",{'i':O1})


# to show update form 
def updtrestf(request,id):
    O1=addrest.objects.get(id=id)
    return render(request,"updtrest.html",{'x':O1})

def updateoffers1f(request,id):
    O1=addoffer.objects.get(id=id)
    return render(request,"updateoffers.html",{'x':O1})

def updatemenu2f(request,id):
    O1=addmenu.objects.get(id=id)
    return render(request,"updatemenuadmin.html",{'x':O1})

def updatefoodadmin1f(request,id):
    O1=addfood.objects.get(id=id)
    return render(request,"updatefoodadmin.html",{'x':O1})

def updateprofile1f(request):
    O1=User.objects.get(is_superuser=1)
    return render(request,"updateprofile.html",{'i':O1})

# for update form action

def updtrest1f(request,id):
    O1=addrest.objects.get(id=id)
    # D1=addrest.objects.get(id=id)

    O1.Restaurant_Name=request.POST.get('rname')
    O1.Location=request.POST.get('loc')
    photo=request.FILES['rimg1'] 
    fs= FileSystemStorage()
    filename=fs.save(photo.name,photo) 
    uploaded_file_url=fs.url(filename)
    O1.Restaurant_Image=uploaded_file_url
    O1.state=request.POST.get('state2')
    O1.Phone=request.POST.get('phone')
    O1.Auth_Person=request.POST.get('person')
    photo=request.FILES['img1'] 
    fs= FileSystemStorage()
    filename=fs.save(photo.name,photo) 
    uploaded_file_url=fs.url(filename)
    O1.Image=uploaded_file_url
    O1.Auth_Email=request.POST.get('aemail')
    O1.Auth_Phone=request.POST.get('aphone')
    O1.username=request.POST.get('uname')

    # D1.Restaurant_Name=request.POST.get('rname')
    # D1.Location=request.POST.get('loc')
    # photo=request.FILES['rimg1'] 
    # fs= FileSystemStorage()
    # filename=fs.save(photo.name,photo) 
    # uploaded_file_url=fs.url(filename)
    # D1.Restaurant_Image=uploaded_file_url
    # D1.state=request.POST.get('state2')
    # D1.Phone=request.POST.get('phone')
   
    O1.save()
    # D1.save()
    return redirect('/viewrest')

def viewupdateofferf(request,id):
    A6=addoffer.objects.get(id=id)
    A6.Restaurant_Name=request.POST.get('rname')
    A6.Menu_Item=request.POST.get('person')
    A6.offer=request.POST.get('moffer')
    A6.Start_Date=request.POST.get('sdate')
    A6.End_Date=request.POST.get('edate')
    A6.Status=request.POST.get('estat')
    A6.save()
    return redirect('/updateoffers')

def updatemenuadmin2f(request,id):
    A4=addmenu.objects.get(id=id)

    A4.Restaurant_Name=request.POST.get('rname')
    A4.Menu_Name=request.POST.get('mname')
    photo=request.FILES['img'] 
    fs= FileSystemStorage()
    filename=fs.save(photo.name,photo) 
    uploaded_file_url=fs.url(filename)
    A4.Image=uploaded_file_url
    A4.cuisin=request.POST.get('uname')
    A4.Type=request.POST.get('veg')
   
    A4.save()
    return redirect('/updatemenuadmin')

def updatefoodadmin2f(request,id):
    A5=addfood.objects.get(id=id)
    
    A5.Restaurant_Name=request.POST.get('rname')
    A5.Menu_Name=request.POST.get('mname')
    A5.Menu_Item=request.POST.get('mitem')
    photo=request.FILES['img'] 
    fs= FileSystemStorage()
    filename=fs.save(photo.name,photo) 
    uploaded_file_url=fs.url(filename)
    A5.Image=uploaded_file_url
    A5.Quantity=request.POST.get('mquant')
    A5.Price=request.POST.get('mprice')
    A5.Cooking_Time=request.POST.get('uname')
    A5.Status=request.POST.get('mstatus')
  

    A5.save()
    return redirect('/updatefoodadmin')

def viewupdateprofile2f(request,id):
    
    
    p1=User.objects.get(is_superuser=1,id=id)
    email=request.POST.get('email')
    u1=useraccount.objects.get(email=email)
    if p1 is not None:

        p1.first_name=request.POST.get('fname')
        p1.last_name=request.POST.get('lname')
        p1.email=request.POST.get('email')
        # p1.username=request.POST.get('uname')
        # to encrypt password
        # password=request.POST.get('pwd')
        # p1.set_password(password)

        p1.save()
    else:
        pass
    
    if u1 is not None:
        u1.userType="admin"
        u1.first_name=request.POST.get('fname')
        u1.last_name=request.POST.get('lname')
        photo=request.FILES['img1'] 
        fs= FileSystemStorage()
        filename=fs.save(photo.name,photo) 
        uploaded_file_url=fs.url(filename)
        u1.Image=uploaded_file_url
        u1.gender="gen"
        u1.Adress=request.POST.get('address')
        u1.Phone=request.POST.get('phone')
        u1.Email=request.POST.get('email')
        u1.state=request.POST.get('State1')
        u1.username=request.POST.get('uname')
        u1.userType="restUser"
        u1.save()
    else:
        User=useraccount()
    return redirect('/admin1')


# to delete
# to show delete table
def deleterestf(request):
    O1=addrest.objects.all()
    return render(request,"deleterest.html",{'x':O1})
def deleteoffersf(request):
    O1=addoffer.objects.all()
    return render(request,"deleteoffers.html",{'x':O1})
def deletemenuadminf(request):
    O1=addmenu.objects.all()
    return render(request,"deletemenuadmin.html",{'x':O1})
def deletefoodadminf(request):
    O1=addfood.objects.all()
    return render(request,"deletefoodadmin.html",{'x':O1})
# delete
def deleterest1f(request,id):
    O1=addrest.objects.get(id=id)
    O1.delete()
    return redirect('/deleterest')
def deleteoffers1f(request,id):
    O1=addoffer.objects.get(id=id)
    O1.delete()
    return redirect('/deleteoffers')
def deletemenuadmin1f(request,id):
    O1=addmenu.objects.get(id=id)
    O1.delete()
    return redirect('/deletemenuadmin')
def deletefoodadmin1f(request,id):
    O1=addfood.objects.get(id=id)
    O1.delete()
    return redirect('/deletefoodadmin')


# go to pages from restprofile to add
def addmenuf(request):
    return render(request,"addmenu.html")
def addfoodf(request):
    return render(request,"addfood.html")

# to view
def viewmenuf(request):
     O1=addmenu.objects.all()
     return render(request,"viewmenu.html",{'x':O1})

def viewfoodf(request):
     O1=addfood.objects.all()
     return render(request,"viewfood.html",{'x':O1})

def viewoffersf(request):
     O1=addoffer.objects.all()
     return render(request,"viewoffers.html",{'x':O1})

def viewfeedbackf(request):
     O1=addfeedback.objects.all()
     return render(request,"viewfeedback.html",{'x':O1})
# def viewfeedbackf(request):
#      O1=addfeedback.objects.all()
#      return render(request,"viewfeedback.html",{'x':O1})

# to update
# to show update table
def viewupdatemenuf(request):
     O1=addmenu.objects.all()
     return render(request,"viewupdatemenu.html",{'x':O1})
def viewupdatefoodf(request):
     O1=addfood.objects.all()
     return render(request,"viewupdatefood.html",{'x':O1})

# to show update form 
def updatemenuf(request,id):
    O1=addmenu.objects.get(id=id)
    return render(request,"updatemenu.html",{'x':O1})
def updatefoodf(request,id):
    O1=addfood.objects.get(id=id)
    return render(request,"updatefood.html",{'x':O1})
# to form action
def updatemenu1f(request,id):
    A4=addmenu.objects.get(id=id)

    A4.Restaurant_Name=request.POST.get('rname')
    A4.Menu_Name=request.POST.get('mname')
    photo=request.FILES['img'] 
    fs= FileSystemStorage()
    filename=fs.save(photo.name,photo) 
    uploaded_file_url=fs.url(filename)
    A4.Image=uploaded_file_url
    A4.cuisin=request.POST.get('uname')
    A4.Type=request.POST.get('veg')
   
    A4.save()
    return redirect('/viewupdatemenu')

def updatefood1f(request,id):
    A5=addfood.objects.get(id=id)
    A5.Restaurant_Name=request.POST.get('rname')
    A5.Menu_Name=request.POST.get('mname')
    A5.Menu_Item=request.POST.get('mitem')
    photo=request.FILES['img'] 
    fs= FileSystemStorage()
    filename=fs.save(photo.name,photo) 
    uploaded_file_url=fs.url(filename)
    A5.Image=uploaded_file_url
    A5.Quantity=request.POST.get('mquant')
    A5.Price=request.POST.get('mprice')
    A5.Cooking_Time=request.POST.get('uname')
    A5.Status=request.POST.get('mstatus')

    A5.save()
    return redirect('/viewupdatefood')

# to delete
#  to show delete tabele
def deletemenuf(request):
    O1=addmenu.objects.all()
    return render(request,"deletemenu.html",{'x':O1})
def deletefoodf(request):
    O1=addfood.objects.all()
    return render(request,"deletefood.html",{'x':O1})
# delete
def deletemenu1f(request,id):
    O1=addmenu.objects.get(id=id)
    O1.delete()
    return redirect('/deletemenu')
def deletefood1f(request,id):
    O1=addfood.objects.get(id=id)
    O1.delete()
    return redirect('/deletefood')



    return render(request,"deletefood.html")

# go to pages from restpublic 
# to add
def addfeedbackf(request):
    return render(request,"addfeedback.html")
# to view
def publicrestf(request):
     O1=addrest.objects.all()
     return render(request,"publicrest.html",{'x':O1})
def publicmenuf(request):
     O1=addmenu.objects.all()
     return render(request,"publicmenu.html",{'x':O1})
def publicfoodf(request):
     O1=addfood.objects.all()
     return render(request,"publicfood.html",{'x':O1})
def publicoffersf(request):
     O1=addoffer.objects.all()
     return render(request,"publicoffers.html",{'x':O1})

def pulicoffers1f(request):
     O1=addoffer.objects.all()
     return render(request,"publicoffers.html",{'x':O1})


# to logout to restlogin
def restloginf(request):
    return render(request,"userlogin.html")



# to auth createadmin

def createuserf(request):
    p1=User()
    A1=useraccount()
    p1.first_name=request.POST.get('fname')
    p1.last_name=request.POST.get('lname')
    p1.email=request.POST.get('email')
    p1.username=request.POST.get('uname')
    # to encrypt password
    password=request.POST.get('pwd')
    p1.set_password(password)

    A1.first_name=request.POST.get('fname')
    A1.last_name=request.POST.get('lname')
    photo=request.FILES['img1'] 
    fs= FileSystemStorage()
    filename=fs.save(photo.name,photo) 
    uploaded_file_url=fs.url(filename)
    A1.Image=uploaded_file_url
    A1.gender=request.POST.get('gen')
    A1.Adress=request.POST.get('address')
    A1.Phone=request.POST.get('phone')
    A1.Email=request.POST.get('email')
    A1.state=request.POST.get('State1')
    A1.username=request.POST.get('uname')
    A1.userType="restUser"
    p1.save()
    A1.save()
    return render(request,"index.html")

# to auth admin login
def loginuserf(request):
    username=request.POST.get('uname')
    password=request.POST.get('pwd')   
    user = authenticate(username=username, password=password)
    # to print in cmd
    print (user,"text1") 
    # supruser authentiaction
    if user is not None and user.is_superuser==1:
        # data=useraccount.objects.get(username=username)

        return render(request,"admin1.html",{'user1':user})
    # normal admin authentication
    elif user is not None:
        data=useraccount.objects.get(username=username)
        if data.userType=="restUser":
            return render(request,"restpublic.html",{'user1':data})
        elif data.userType=="restAdmin":
            data1=addrest.objects.get(username=username)
            return render(request,"restprofile.html",{'user1':data,"datas":data1})
        else:
            return HttpResponse("Invalid user")
    else:
        return HttpResponse("Invalid user")

def addrest1f(request):
    A2=addrest()
    p1=User()
    A1=useraccount()
    A3=viewrest()
    # p1.first_name=request.POST.get('fname')
    # p1.last_name=request.POST.get('lname')
    p1.email=request.POST.get('aemail')
    p1.username=request.POST.get('uname')
    # to encrypt password
    password=request.POST.get('pwd')
    p1.set_password(password)
    
    A1.first_name="first"
    A1.last_name="last"
    photo=request.FILES['img1'] 
    fs= FileSystemStorage()
    filename=fs.save(photo.name,photo) 
    uploaded_file_url=fs.url(filename)
    A1.Image=uploaded_file_url
    A1.gender="Others"
    A1.Adress=request.POST.get('loc')
    A1.Phone=request.POST.get('phone')
    A1.Email=request.POST.get('email')
    A1.state=request.POST.get('state2')
    A1.username=request.POST.get('uname')
    A1.userType="restAdmin"
    
    
    A2.Restaurant_Name=request.POST.get('rname')
    A2.Location=request.POST.get('loc')
    photo=request.FILES['rimg1'] 
    fs= FileSystemStorage()
    filename=fs.save(photo.name,photo) 
    uploaded_file_url=fs.url(filename)
    A2.Restaurant_Image=uploaded_file_url
    A2.state=request.POST.get('state2')
    A1.Email=request.POST.get('email')
    A2.Phone=request.POST.get('phone')
    A2.Auth_Person=request.POST.get('person')
    photo=request.FILES['img1'] 
    fs= FileSystemStorage()
    filename=fs.save(photo.name,photo) 
    uploaded_file_url=fs.url(filename)
    A2.Image=uploaded_file_url
    A2.Auth_Email=request.POST.get('aemail')
    A2.Auth_Phone=request.POST.get('aphone')
    A2.username=request.POST.get('uname')

    A3.Restaurant_Name=request.POST.get('rname')
    A3.Location=request.POST.get('loc')
    photo=request.FILES['rimg1'] 
    fs= FileSystemStorage()
    filename=fs.save(photo.name,photo) 
    uploaded_file_url=fs.url(filename)
    A3.Restaurant_Image=uploaded_file_url
    A3.state=request.POST.get('state2')
    A3.Phone=request.POST.get('phone')
   
    p1.save()
    A1.save()
    A2.save()
    A3.save()
    return render(request,"admin1.html")
   
def addmenu1f(request):
    A4=addmenu()

    A4.Restaurant_Name=request.POST.get('rname')
    A4.Menu_Name=request.POST.get('mname')
    photo=request.FILES['img'] 
    fs= FileSystemStorage()
    filename=fs.save(photo.name,photo) 
    uploaded_file_url=fs.url(filename)
    A4.Image=uploaded_file_url
    A4.cuisin=request.POST.get('uname')
    A4.Type=request.POST.get('veg')
   
    A4.save()
    return render(request,"restprofile.html")

def addfood1f(request):
    A5=addfood()

    A5.Restaurant_Name=request.POST.get('rname')
    A5.Menu_Name=request.POST.get('mname')
    A5.Menu_Item=request.POST.get('mitem')
    photo=request.FILES['img'] 
    fs= FileSystemStorage()
    filename=fs.save(photo.name,photo) 
    uploaded_file_url=fs.url(filename)
    A5.Image=uploaded_file_url
    A5.Quantity=request.POST.get('mquant')
    A5.Price=request.POST.get('mprice')
    A5.Cooking_Time=request.POST.get('uname')
    A5.Status=request.POST.get('mstatus')
  
    A5.save()
    return render(request,"addfood.html")

def addoffer1f(request):
    A6=addoffer()

    A6.Restaurant_Name=request.POST.get('rname')
    A6.Menu_Item=request.POST.get('person')
    A6.offer=request.POST.get('moffer')
    A6.Start_Date=request.POST.get('sdate')
    A6.End_Date=request.POST.get('edate')
    A6.Status=request.POST.get('estat')
  
    A6.save()
    return render(request,"addoffers.html")

def addfeedback1f(request):
    A7=addfeedback()

    A7.Restaurant_Name=request.POST.get('rname')
    A7.Customer_Name=request.POST.get('person')
    A7.Feedback=request.POST.get('edate')
    A7.Date=request.POST.get('estat')
  
    A7.save()
    return render(request,"addfeedback.html")