"""promain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
# go to pages from index
    path('',views.indexf),
    path('usercreate/',views.usercreatef),
    path('createuser/',views.createuserf),
    path('userlog/',views.userlogf),
    path('admincreate/',views.admincreatef),
    path('adminlogin/',views.adminloginf),
    path('restpublic/',views.restpublicf),
    path('viewmenuindex/',views.viewmenuindexf),
    path('viewoffersindex/',views.viewoffersindexf),
    path('viewrestindex/',views.viewrestindexf),


# go to pages from admin1 to add
    path('addrest/',views.addrestf),
    path('addoffers/',views.addoffersf),

    # action
    path('addrest1/',views.addrest1f),
    path('addoffer1/',views.addoffer1f),
    

    # to view
    path('viewrest/',views.viewrestf),
    path('Viewprofile/',views.Viewprofilef),
    path('viewmenuadmin/',views.viewmenuadminf),
    path('viewfoodadmin/',views.viewfoodadminf),
    path('viewoffersadmin/',views.viewoffersadminf),
    path('viewfeedbackadmin/',views.viewfeedbackadminf),

# to show update table
    path('viewupdaterest/',views.viewupdaterestf),
    path('updateoffers/',views.updateoffersf),
    path('updatemenuadmin/',views.updatemenuadminf),
    path('updatefoodadmin/',views.updatefoodadminf),
    path('updateprofile/',views.updateprofilef),


   
# to show update form 
    path('updtrest/<int:id>',views.updtrestf),
    path('updateoffers1/<int:id>',views.updateoffers1f),
    path('updatemenu2/<int:id>',views.updatemenu2f),
    path('updatefoodadmin1/<int:id>',views.updatefoodadmin1f),
    path('updateprofile1/',views.updateprofile1f),


    # update form action
    path('updtrest1/<int:id>',views.updtrest1f),
    path('updateoffers/<int:id>',views.viewupdateofferf),
    path('updatemenuadmin/<int:id>',views.updatemenuadmin2f),
    path('updatefoodadmin/<int:id>',views.updatefoodadmin2f),
    path('updateAdminProfile/<int:id>',views.viewupdateprofile2f),


    
    # to delete
    # to show delete table
    path('deleterest/',views.deleterestf),
    path('deleteoffers/',views.deleteoffersf),
    path('deletemenuadmin/',views.deletemenuadminf),
    path('deletefoodadmin/',views.deletefoodadminf),


    # delete
    path('deleterest1/<int:id>',views.deleterest1f),
    path('deleteoffers1/<int:id>',views.deleteoffers1f),
    path('deletemenuadmin1/<int:id>',views.deletemenuadmin1f),
    path('deletefoodadmin1/<int:id>',views.deletefoodadmin1f),


# logout to restlogin
    path('restlogin/',views.restloginf),


# to authenticate user login
    path('loginuser/',views.loginuserf),
    
# go to pages from restprofile 

# to add
   path('addmenu/',views.addmenuf),
   path('addfood/',views.addfoodf),

#    to action
   path('addmenu1/',views.addmenu1f),
   path('addfood1/',views.addfood1f),


#    to view
   
   path('viewmenu/',views.viewmenuf),
   path('viewfood/',views.viewfoodf),
   path('viewoffers/',views.viewoffersf),
   path('viewfeedback/',views.viewfeedbackf),

# to show update table
   path('viewupdatemenu/',views.viewupdatemenuf),
   path('viewupdatefood/',views.viewupdatefoodf),

# to show update form   
   path('updatemenu/<int:id>',views.updatemenuf),
   path('updatefood/<int:id>',views.updatefoodf),

    # update form action
   path('updatemenu1/<int:id>',views.updatemenu1f),   
   path('updatefood1/<int:id>',views.updatefood1f),   

#    to delete
 # to show delete table
   path('deletemenu/',views.deletemenuf),
   path('deletefood/',views.deletefoodf),   
#    delete
    path('deletemenu1/<int:id>',views.deletemenu1f),
    path('deletefood1/<int:id>',views.deletefood1f),   

  
 
   # go to pages from restpublic 
#    to add
   path('addfeedback/',views.addfeedbackf),
#    action feedback   
   path('addfeedback1/',views.addfeedback1f),

#    to view
   path('publicrest/',views.publicrestf),   
   path('publicmenu/',views.publicmenuf),   
   path('publicfood/',views.publicfoodf), 
   path('publicoffers/',views.publicoffersf),   
   path('pulicoffers1/',views.pulicoffers1f),   




]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)