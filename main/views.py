########################################### important import ########################################################################

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from . models import saleData,expanceData,contact
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Sum

# Create your views here.

def index(request):
    if request.method == 'POST':
        date = request.POST['date']
        cosName = request.POST['cosName']
        phone = request.POST['phone']
        email = request.POST['email']
        serviceName = request.POST['serviceName']
        price = request.POST['price']

        if len(cosName)<5:
            messages.error(request,'Costumer name is too short plase try agin later.')
            return redirect('index')

        if len(phone)<10:
            messages.error(request,'Phone number not valid please try agian later.')
            return redirect('index')

        if len(phone)>10:
            messages.error(request,'Phone number not valid please try agian later.')
            return redirect('index')

        if len(serviceName)<2:
            messages.error(request,'service name is too short please try again later.')
            return redirect('index')

        if len(price)<1:
            messages.error(request,'not valid price please try again later.')
            return redirect('index')
        else:
            saledata = saleData(date=date,cosName=cosName,phone=phone,email=email,serviceName=serviceName,price=price)
            saledata.usr = request.user
            saledata.save()
            messages.success(request,'Your valuse are successfuly save.')
            return redirect('index')

    if not request.user.is_authenticated:
        return render(request,'index.html')

    else:              
        noSale = saleData.objects.filter(usr=request.user).count()
        if noSale != None:
            sellData = {'noSale':noSale}
            return render(request,'index.html',sellData)
        noExp = expanceData.objects.filter(usr=request.user).count()
        if noExp !=None:
            buyData = {'noExp':noExp}
            return render(request,'index.html',buyData)

        lastSale = saleData.objects.filter(usr=request.user).all().aggregate(Sum('price'))['price__sum']
        if lastSale !=None:
            lastSaleData = {'lastSale':lastSale}
            return render(request,'index.html',lastSaleData)

        lastExp = expanceData.objects.filter(usr=request.user).all().aggregate(Sum('price'))['price__sum']
        if lastSale and lastExp != None:
            profitLoss = lastSale - lastExp
        else:
            return render(request,'index.html')         
        params = {'profitLoss':profitLoss,'noSale':noSale,'noExp':noExp}
        return render(request,'index.html',params)   
    
def expance(request):
    if request.method == 'POST':
        date = request.POST['date']
        buyerName = request.POST['buyerName']
        buyerPhone = request.POST['buyerPhone']
        buyerEmail = request.POST['buyerEmail']
        serviceName = request.POST['serviceName']
        price = request.POST['price']

        if len(buyerName)<4:
            messages.error(request,'Buyer Name is too short please try again.')
            return redirect('index')

        if len(buyerPhone)<10:
            messages.error(request,'not a valid number please try again later.')
            return redirect('index')

        if len(buyerPhone)>10:
            messages.error(request,'not a valid number please try again later.')
            return redirect('index')    


        if len(serviceName)<3:
            messages.error(request,'service name is too short please try again later.')
            return redirect('index')

        if len(price)<1:
            messages.error(request,'price is too short please try again later.')
            return redirect('index')

        else:
            expancedata = expanceData(date=date,buyerName=buyerName,buyerPhone=buyerPhone,buyerEmail=buyerEmail,serviceName=serviceName,price=price)
            expancedata.usr = request.user
            expancedata.save()
            messages.success(request,'your values are successfuly save.')
            return render(request,'index.html')                
    return render(request,'index.html')            

def help(request):
    if not request.user.is_authenticated:
        return render(request,'help.html')

    else:
        noSale = saleData.objects.filter(usr=request.user).count()
        noExp = expanceData.objects.filter(usr=request.user).count()
        lastSale = saleData.objects.filter(usr=request.user).all().aggregate(Sum('price'))['price__sum']
        lastExp = expanceData.objects.filter(usr=request.user).all().aggregate(Sum('price'))['price__sum']
        if lastSale and lastExp != None:
            profitLoss = lastSale - lastExp
        else:
            return render(request,'help.html')   
        params = {'profitLoss':profitLoss,'noSale':noSale,'noExp':noExp,'lastSale':lastSale,'lastExp':lastExp}
        return render(request,'help.html',params)

def contactUs(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        quary = request.POST['quary']

        if len(name)<3:
            messages.error(request,"You name is too short plase try anouther name.")
            return render(request,'contactUs.html')
        if len(phone)<10:
            messages.error(request,'Phone number not valid please try again.')
            return render(request,'contactUs.html')
        if len(phone)>10:
            messages.error(request,'Phone number not valid plase try agin.')
            return render(request,'contactUs.html')
        if len(address)<5:
            messages.error(request,'Address is too short please try agin later.')
            return render(request,'contactUs.html')
        if len(quary)<5:
            messages.error(request,'Quary is too short please try agin later.')
            return render(request,'contactUs.html')

        else:
            contact_view = contact(name=name,phone=phone,email=email,address=address,quary=quary)
            contact_view.usr = request.user
            contact_view.save()
            messages.success(request,'Your quary has been submited sucessfuly.')
            return render(request,'contactUs.html')

    if not request.user.is_authenticated:
        return render(request,'contactUs.html')

    else:            
        noSale = saleData.objects.filter(usr=request.user).count()
        noExp = expanceData.objects.filter(usr=request.user).count()
        lastSale = saleData.objects.filter(usr=request.user).all().aggregate(Sum('price'))['price__sum']
        lastExp = expanceData.objects.filter(usr=request.user).all().aggregate(Sum('price'))['price__sum']
        if lastSale and lastExp != None:
            profitLoss = lastSale - lastExp
        else:
            return render(request,'contactUs.html')    
        params = {'profitLoss':profitLoss,'noSale':noSale,'noExp':noExp,'lastSale':lastSale,'lastExp':lastExp}
        return render(request,'contactUs.html',params)    

def search(request):
    return render(request,'search.html')


############################################### LogIn Function start here #################################################################


def logIn(request):
    if request.method == 'POST':
        userName = request.POST['userName']
        passWord = request.POST['password']

        if len(userName)<5:
            messages.error(request,'your username is too short, please chose atleste 5 charcter in your username.')
            return redirect('/')

        if len(passWord)<5:
            messages.error(request,'your password is too short please try again.')
            return redirect('/')
            
        user = authenticate(request,username=userName, password=passWord)

        if user is not None:
            login(request, user)
            messages.success(request,"you are successful login.")
            return redirect('index')
        else:
            messages.error(request,'Somethig want worng please try again later.')
            return redirect('/')
    
    if not request.user.is_authenticated:
        return render(request,'logIn.html')

    else:    
        noSale = saleData.objects.filter(usr=request.user).count()
        noExp = expanceData.objects.filter(usr=request.user).count()
        lastSale = saleData.objects.filter(usr=request.user).all().aggregate(Sum('price'))['price__sum']
        lastExp = expanceData.objects.filter(usr=request.user).all().aggregate(Sum('price'))['price__sum']
        if lastSale and lastExp != None: 
            profitLoss = lastSale - lastExp
        else:
            return render(request,'logIn.html')  
        params = {'profitLoss':profitLoss,'noSale':noSale,'noExp':noExp,'lastSale':lastSale,'lastExp':lastExp}            
        return render(request,'logIn.html',params)


##################################################### LogOut function start here ##############################################################  

def logOut(request):
    logout(request)
    messages.success(request,'you are successful logout.')
    return redirect('/')       


def report(request):
    if not request.user.is_authenticated:
        return render(request,'report.html')

    else:    
        noSale = saleData.objects.filter(usr=request.user).count()
        noExp = expanceData.objects.filter(usr=request.user).count()
        lastSale = saleData.objects.filter(usr=request.user).aggregate(Sum('price'))['price__sum']
        print(lastSale)
        lastExp = expanceData.objects.filter(usr=request.user).aggregate(Sum('price'))['price__sum'] 
        fachSale = saleData.objects.filter(usr=request.user)
        fachExp = expanceData.objects.filter(usr=request.user)  
        if lastSale and lastExp != None:
            profitLoss = lastSale - lastExp  
        else:
            return render(request,'report.html')
        params = {'profitLoss':profitLoss,'noSale':noSale,'noExp':noExp,'lastSale':lastSale,'lastExp':lastExp,'fachSale':fachSale,'fachExp':fachExp}
        return render(request,'report.html',params)