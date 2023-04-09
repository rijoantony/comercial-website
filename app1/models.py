from django.db import models


class useraccount(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    Phone=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Image=models.CharField(max_length=500)
    Adress=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    userType=models.CharField(max_length=20)

    class meta:
        db_table="useraccount"

class addrest(models.Model):
    # first_name=models.CharField(max_length=50)
    # last_name=models.CharField(max_length=50)
    Restaurant_Name=models.CharField(max_length=50)
    Location=models.CharField(max_length=50)
    Restaurant_Image=models.CharField(max_length=500)
    state=models.CharField(max_length=50)
    Phone=models.CharField(max_length=50)
    Auth_Person=models.CharField(max_length=50)
    Image=models.CharField(max_length=500)
    Auth_Email=models.CharField(max_length=50)
    Auth_Phone=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)


    class meta:
        db_table="addrest"

class viewrest(models.Model):
    Restaurant_Name=models.CharField(max_length=50)
    Location=models.CharField(max_length=50)
    Restaurant_Image=models.CharField(max_length=500)
    state=models.CharField(max_length=50)
    Phone=models.CharField(max_length=50)
    
    class meta:
        db_table="viewrest"

class addmenu(models.Model):
    Restaurant_Name=models.CharField(max_length=50)
    Menu_Name=models.CharField(max_length=50)
    Image=models.CharField(max_length=500)
    cuisin=models.CharField(max_length=50)
    Type=models.CharField(max_length=50)
    
    class meta:
        db_table="addmenu"

class addfood(models.Model):
    Restaurant_Name=models.CharField(max_length=50)
    Menu_Name=models.CharField(max_length=50)
    Menu_Item=models.CharField(max_length=50)
    Image=models.CharField(max_length=500)
    Quantity=models.CharField(max_length=50)
    Price=models.CharField(max_length=50)
    Cooking_Time=models.CharField(max_length=50)
    Status=models.CharField(max_length=50)


    class meta:
        db_table="addfood"

class addoffer(models.Model):
    Restaurant_Name=models.CharField(max_length=50)
    Menu_Item=models.CharField(max_length=50)
    offer=models.CharField(max_length=50)
    Start_Date=models.CharField(max_length=50)
    End_Date=models.CharField(max_length=50)
    Status=models.CharField(max_length=50)
    
    class meta:
        db_table="addoffer"

class addfeedback(models.Model):
    Restaurant_Name=models.CharField(max_length=50)
    Customer_Name=models.CharField(max_length=50)
    Feedback=models.CharField(max_length=50)
    Date=models.CharField(max_length=50)
    
    class meta:
        db_table="addfeedback"

# Create your models here.
