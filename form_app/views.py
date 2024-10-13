

# Create your views here.
from django.shortcuts import render, redirect
from .forms import ContactForm
from .forms import CustomContactForm
from .models import Contact


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Automatically saves to the database
            return redirect('success')
    else:
        form = ContactForm()

    return render(request, 'form_app/contact.html', {'form': form})


def success_view(request):
    return render(request, 'form_app/success.html')



def custom_contact_view(request):
    if request.method == 'POST':
        form = CustomContactForm(request.POST)
        if form.is_valid():
            # 
            # Process the form data manually
            c=Contact(
            name = form.cleaned_data['name'],
            email = form.cleaned_data['email'],
            message = form.cleaned_data['message']
            )
            c.save()
            
            # form.save()

            # (You could store this data in the database or process it)
            return redirect('success')
    else:
        form = CustomContactForm()

    return render(request, 'form_app/custom_contact.html', {'form': form})

