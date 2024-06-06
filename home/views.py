from django.shortcuts import render,redirect
from home.models import *
from about.models import *
from services.models import *
from book.models import *
from gallery.models import *
from contact.models import *

from django.contrib import messages

# Create your views here.

def index(request):
    header = Header.objects.first()
    services = Service_content.objects.all()
    whatshappening=WhatsHappening.objects.all()

    context={
        'header':header,
        'services':services,
        'whatshappening':whatshappening,

    }
    return render(request,"index.html",context)

def about_us(request):
    background=About_Background.objects.first()
    images=About_Images.objects.all()
    content=About_Content.objects.first()

    context={
        'background':background,
        'content':content,
        'images':images
    }
    return render(request,"about_us.html",context)

def services(request):
    categories = ServiceCategory.objects.prefetch_related('services').all()
    background=Background_content.objects.first()

    context={
        'categories': categories,
        'background':background

    }
    return render(request, 'services.html', context)

def book_it(request):

    images=Background_Images.objects.first()
    contents=Body_Content.objects.first()

    context={
        'images':images,
        'contents':contents
    }

    if request.method == "POST":

        errors = []


        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')  # Corrected typo
        telephone_number = request.POST.get('telephonenumber')
        email = request.POST.get('email')
        style_needed = request.POST.get('styleneeded')
        appointment_date = request.POST.get('date')
        appointment_time = request.POST.get('time')
        street_address = request.POST.get('streetaddress')
        like_website = request.POST.get('likeit')
        find_us = request.POST.get('findus')
        comments = request.POST.get('comments')

        # Manual validation
        if not first_name:
            errors.append('First name is required.')
        if not last_name:
            errors.append('Last name is required.')
        if not telephone_number:
            errors.append('Telephone number is required.')
        if not email:
            errors.append('Email is required.')
        if not style_needed:
            errors.append('Style needed is required.')
        if not appointment_date:
            errors.append('Appointment date is required.')
        if not appointment_time:
            errors.append('Appointment time is required.')
        if not street_address:
            errors.append('Street address is required.')
        if not like_website:
            errors.append('Please let us know if you like this website.')
        if not find_us:
            errors.append('Please let us know how you found us.')
        if not comments:
            errors.append('Comments are required.')

        # If there are errors, show them
        if errors:
            for error in errors:
                messages.error(request, error)
            return render(request, 'book_it.html')


        
         # Save to database
        appointment = Book_Appointment(
            first_name=first_name,
            last_name=last_name,
            telephone_number=telephone_number,
            email=email,
            style_needed=style_needed,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            street_address=street_address,
            like_website=like_website,
            find_us=find_us,
            comments=comments
        )
        appointment.save()
        messages.success(request, 'Your appointment has been booked successfully!')

    return render(request,"book_it.html",context)


def gallery(request):
    contents=Content.objects.first()
    images=Gallery_Images.objects.all()

    context={
        'contents':contents,
        "images":images
    }
    return render(request,"gallery.html",context)

def contact_us(request):
    contents=Contact_Background.objects.first()
    info=ContactInfo.objects.first()
    body=Body.objects.first()

    context={
        'contents':contents,
        'info':info,
        'body':body
    }

    if request.method == "POST":

        errors = []


        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')  # Corrected typo
        telephone_number = request.POST.get('telephonenumber')
        email = request.POST.get('email')
        code=request.POST.get('code')
        comments=request.POST.get('comments')

        # Manual validation
        if not first_name:
            errors.append('First name is required.')
        if not last_name:
            errors.append('Last name is required.')
        if not telephone_number:
            errors.append('Telephone number is required.')
        if not email:
            errors.append('Email is required.')
        if not comments:
            errors.append('Comments are required.')

        # If there are errors, show them
        if errors:
            for error in errors:
                messages.error(request, error)
            return render(request, 'contact_us.html')


        
         # Save to database
        data = ContactFormSubmission(
            first_name=first_name,
            last_name=last_name,
            telephone_number=telephone_number,
            email=email,
            comments=comments
        )
        data.save()
        messages.success(request, 'Your Form has been Submitted Successfully!')

    return render(request,"contact_us.html",context)
