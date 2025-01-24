from django.shortcuts import render,redirect
from .models import Form
# Create your views here.
def home(request):
    mydata=Form.objects.all()
    if(mydata!=''):
        return render(request,'home.html',{'datas':mydata})
    else:
        return render(request,'home.html')
def adddata(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        contact=request.POST['contact']
        mail=request.POST['mail']
        
        obj=Form()
        obj.Name=name
        obj.Age=age
        obj.Address=address
        obj.Contact=contact
        obj.Email=mail 
        obj.save()
        mydata=Form.objects.all()
        return redirect('home')
    return render(request,'home.html')
def updatedata(request,id):
    mydata=Form.objects.get(id=id)
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        contact=request.POST['contact']
        mail=request.POST['mail']
        
        mydata.Name=name 
        mydata.Age=age
        mydata.Address=address
        mydata.Contact=contact
        mydata.Email=mail
        mydata.save()
        return redirect('home')    
    return render(request,'update.html',{'data':mydata})
def deletedata(request,id):
    mydata=Form.objects.get(id=id)
    mydata.delete()
    return redirect('home')
def login(request):
    if request.method == 'POST':
        email = request.POST['email'].strip().lower()  # Normalize the email
        
        mydata = Form.objects.all()  # Fetch all data from Form model
        
        # Check if the email exists in the database
        for user in mydata:
            if user.Email.strip().lower() == email:
                return render(request, 'home.html')
        
        return render(request,"error.html")
    
    return render(request, "login.html")
