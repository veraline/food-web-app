from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect  
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_protect

@ensure_csrf_cookie
@csrf_protect
def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def About(request):
    template = loader.get_template('About.html')
    return HttpResponse(template.render())

def services(request):
    template = loader.get_template('service.html')
    return HttpResponse(template.render())

def menu(request):
    template = loader.get_template('menu.html')
    return HttpResponse(template.render())


def Login(request):
    template = loader.get_template('Login.html')
    return HttpResponse(template.render())

def Signin(request):
    template = loader.get_template('Signin.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

def booking(request):
    template = loader.get_template('booking.html')
    return HttpResponse(template.render())

def testimonial(request):
    template = loader.get_template('testimonial.html')
    return HttpResponse(template.render())

def team(request):
    template = loader.get_template('team.html')
    return HttpResponse(template.render())

# def signin(request):
#     if request.method == 'POST':
#         # Get the form data
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         pass1 = request.POST.get('password')
#         pass2 = request.POST.get('confirm_password')

#         # Save the email in session for later use
#         # request.session['signin_email'] = email
#         # request.session['sigin_password'] = password
#         if pass1 != pass2:
#             return HttpResponse('your passwords does not match')
#         else:
#             my_user = User.objects.create_user(name, email, pass1)
#             my_user.save()

#             return redirect('login')  # Redirect to the login page

#     return render(request, 'Signin.html')

def signin(request):
    if request.method == 'POST':
        # Retrieve form data from the request
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        terms = request.POST.get('terms', False)

 # Perform form validation
        if not name or not email or not password or not confirm_password:
            error_message = "Please fill in all the required fields."
            return render(request, 'Signin.html', {'error_message': error_message})
        
        if password != confirm_password:
            error_message = "Password and Confirm Password do not match."
            return render(request, 'Signin.html', {'error_message': error_message})


        # Create a new User object and save it to the database
        user = User(name=name, email=email, password=password, confirm_password=confirm_password, terms=terms)
        user.save()

        # Optionally, you can redirect the user to a success page
        return render(request, 'login')
    else:
        return render(request, 'Signin.html')


def login(request):
    if request.method == 'POST':
        # Get the form data
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Retrieve the email from the session
        signin_email = request.session.get('signin_email')


        if email == signin_email:
            # Authenticate the user
            user = authenticate(request, email=email, password=password)

            if user is not None:
                # Log in the user
                login(request, user)
                return redirect('home')  # Replace 'home' with the URL name of your home page

        # If the authentication fails or the email doesn't match, display an error message
        error_message = 'Invalid email or password.'
        return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'Login.html')