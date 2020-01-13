from django.shortcuts import render
from .models import ContactData
from .forms import ContactForm
from django.http.response import HttpResponse
def Contactview(request):
    if request.method== "POST":
        cform=ContactForm(request.POST)
        if cform.is_valid():
            name1= request.POST.get("name")
            salary1= request.POST.get("salary")
            email1= request.POST.get("email")
            mobile1= request.POST.get("mobile")
            location1= request.POST.get("location")
            data= ContactData(
                name=name1,
                salary= salary1,
                email= email1,
                mobile= mobile1,
                location= location1,
            )
            data.save()
            cform= ContactForm()
            return render(request,'contactform.html',{'abcd':cform})
        else:
            return HttpResponse("User Missing Somevalues")
    else:
        cform= ContactForm()
        return render(request,'contactform.html',{'abcd':cform})


