from django.shortcuts import render,HttpResponse
from datetime import datetime

from home.models import Contact
from django.contrib import messages

# Create your views here.
def web(request):
    # messages.success(request, 'Your messages has been sewnt')
    return render(request,'web.html')
   #context is set of varibles which sent to template
    #context={'variable1':'this is scent',
   # 'variable2':23}
    #return render(request,'index.html',context)
    #return render(request,'index.html',{'variable':'This is scent'})
    #return render(request,'html',{'name':'Garima'})
    #return HttpResponse('<h1>this is homepage!!</h1>')    

def about(request):
    return render(request,'about.html',)
    #return HttpResponse('<h1>this is about page!!</h1>')

def services(request):
    return render(request,'services.html',)
    #return HttpResponse('<h1>this is services page!!</h1>')

def contact(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        #making a contact object
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date= datetime.today())
        contact.save()
        messages.success(request, 'Your messages has been sent!!')
    return render(request,'contact.html')
    #return HttpResponse('<h1>this is contact page!!</h1>')