from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.urls import reverse
from my_portfolio.models import ContactForm

# Create your views here.
def home(request):
    return render(request,'my_portfolio/home.html')

def portfolio(request):
    return render(request,'my_portfolio/portfolio.html')

def contact(request):
    return render(request,'my_portfolio/contact.html')

def contact_form_submit(request):
    if request.method == "POST":
        full_name = request.POST['full_name']
        email_id = request.POST['email_id']
        contact_number = request.POST['contact_number']
        message = request.POST['message']
        ContactForm.objects.create(full_name=full_name,
                                   email_id=email_id,
                                   contact_number=contact_number,
                                   message=message
                                   )
    return HttpResponseRedirect(reverse('my_portfolio:contact'))