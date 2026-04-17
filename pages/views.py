from django.shortcuts import render
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def about_me_view(request):
    return render(request, 'pages/about_me.html')

def experience_view(request):
    return render(request, 'pages/experience.html')

def projects_view(request):
    return render(request, 'pages/projects.html')

def blog_view(request):
    return render(request, 'pages/blog.html')

def contact_view(request):
    # means the form is submitted and not empty
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # collect the data from the form and send email
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Build the full email content
            message_body =(
                f'You have received a new message from your portfolio \n'
                f'Name: {name}\n'
                f'Email: {email}\n'
                f'Message: {message}'
            )
            try:
                # Send the email using Django's send_mail function
                send_mail(
                    "Email From Portfolio",
                    message_body,
                    settings.DEFAULT_FROM_EMAIL,
                    ['struitt.sdgku@gmail.com']
                )
                # If the email is send successfully, you can add a success message
                form = ContactForm()
                return render(request, 'pages/contact.html', {'form': form})
            except Exception as e:
                print(f"Error sending email: {e}")
                return render(request, 'pages/contact.html', {'form': form})
        else:
            print("Form is not valid")
            print(form.errors)
            return render(request, 'pages/contact.html', {'form': form})   
    else:
        form = ContactForm()
        return render(request, 'pages/contact.html', {'form': form})