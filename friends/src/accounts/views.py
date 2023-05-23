from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http import HttpResponse
from .models import Account, User
from django.contrib.auth import authenticate , login, logout
from django.contrib import messages
from main.validators import *
from main.utils import usernameGenerator, get_random_password, get_random_number, uploadToGoogleDrive
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .forms import UpdateForm, passwordChangeForm
from posts.models import Post
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os



def publicProfile_view(request, username):
    template_name = 'accounts/public_profile.html'

    qs = User.objects.filter(username=username)
    if qs.exists():
        user      = User.objects.get(username=username)
        account   = Account.objects.get(user=user)
        post_list = Post.objects.all().filter(account=account).filter(is_active=True)
    else:
        msg = username + ' is not associated with any account!'
        messages.warning(request, msg)
        return HttpResponseRedirect('/404-not-found/')

    paginator = Paginator(post_list, 5) # posts per page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    contex = {
        'account': account,
        'posts': posts
    }

    return render(request, template_name, contex)






def passwordForgot_view(request):
    template_name = 'accounts/forgot-password.html'
    email = request.GET.get('email', None)
    code = None
    message = ""
    if email != None:
        qs = User.objects.filter(email=email)
        if qs.exists():
            account = Account.objects.get(user=User.objects.get(email=email))
            code = account.forgotpass_code
        else:
            message = "No account found associated with this email."
            email = None
    if request.method == "POST":
        input_code = request.POST['a_code']
        if input_code != code:
            message = "Code you entered didn't match!"
        if input_code == code:
            new_passwd = get_random_password()
            user = User.objects.get(email=email)
            user.set_password(raw_password=new_passwd)
            user.save()
            msg = "Your password has been set to <span class='text-danger font-weight-bold'>" + str(new_passwd) + "</span>"
            messages.success(request, msg)
            return redirect('/accounts/login/')
    if email == None:
        form = 'email'
    else:
        form = 'code'

    contex = {
        'email': email,
        'form': form,
        'message': message
    }
    return render(request, template_name, contex)


@login_required
def passwordChange_view(request):
    template_name = 'accounts/change-password.html'
    form = passwordChangeForm(request.user, request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = User.objects.get(email=request.user.email)
            user.set_password(raw_password=form.cleaned_data.get('new'))
            user.save()
            messages.success(request, user.get_full_name() + ', Your password has been updated successfully.')
            return redirect('/accounts/change-password/')
    contex = {
        'form': form
    }
    return render(request, template_name, contex)



@login_required
def update_view(request):
    try:
        account = Account.objects.get(user=request.user)
    except:
        account = None
    if account == None:
        messages.warning(request, 'Account not found!')
        return redirect('/accounts/')
    form = UpdateForm(account, request.POST or None, request.FILES or None, auto_id=False)
    if request.method == "POST":
        if form.is_valid():
            user = User.objects.get(email=request.user.email)
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name  = form.cleaned_data.get('last_name')
            user.save()
            account.about_me = form.cleaned_data.get('about_me')
            if form.cleaned_data.get('photo') != None:
                account.photo = form.cleaned_data.get('photo')
            print(form.cleaned_data.get('photo'))
            account.save()
            if os.path.exists(account.photo.path):
                drive_id = uploadToGoogleDrive(account.photo.path, 'PROFILE')
            if drive_id != "":
                account.drive_photo_link = "https://drive.google.com/thumbnail?id=" + str(drive_id)
                account.save()
            messages.success(request, 'Yahoo! Your information has been updated.')
            return redirect('/accounts/update/')
    template_name = 'accounts/edit.html'
    contex = {
        'form': form,
        'account': account
    }

    return render(request, template_name, contex)

@login_required
def profile_view(request):
    template_name = 'accounts/profile.html'
    try:
        account = Account.objects.get(user=request.user)
    except:
        return HttpResponseRedirect('/404-not-found/')

    post_list = Post.objects.all().filter(is_active=True).filter(account=account)
    paginator = Paginator(post_list, 5) # posts per page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    contex = {
    	'account': account,
    	'posts': posts
    }
    return render(request, template_name, contex)




def activateAccount_view(request):
    template_name = 'accounts/activate.html'
    email = request.GET.get('email', None)
    code = None
    message = ""
    if email != None:
        qs = User.objects.filter(email=email)
        if qs.exists():
            account = Account.objects.get(user=User.objects.get(email=email))
            if not account.is_active:
                code = account.activation_code
            else:
                messages.success(request, "Your account is activated.")
                return redirect('/posts/')
        else:
            message = "No account found associated with this email."
            email = None
    if request.method == "POST":
        input_code = request.POST['a_code']
        if input_code != code:
            message = "Code you entered didn't match!"
        if input_code == code:
            account.is_active = True
            account.save()
            messages.success(request, "Congrats! Your account has been activated.")
            return redirect('/accounts/login/')
    if email == None:
        form = 'email'
    else:
        form = 'code'

    contex = {
        'email': email,
        'form': form,
        'message': message
    }
    return render(request, template_name, contex)

@login_required
def userLogout_view(request):
	next = request.GET.get('next', '/')
	if request.user.is_authenticated:
		logout(request)
		messages.success(request, "You have been logged out.")
	return redirect(next)

def userLogin_view(request):
    next = request.GET.get('next', '/')
    if request.user.is_authenticated:
        return redirect(next)
    template_name = 'accounts/login.html'
    contex = {}
    error  = ""
    if request.is_ajax() and request.method == "POST":
        email = request.POST['username']
        password = request.POST['password']
        if email == '' or password == '':
            error = 'Both fields are required.'
        else:
            qs = User.objects.filter(email=email).exists()
            if qs:
                user = User.objects.get(email=email)
                if not user.check_password(raw_password=password):
                    error = "Username or password incorrect"
            else:
                error = "Username or password incorrect"
        if error == '':
            user = authenticate(request, username=user.username, password=password)
            login(request, user)
            account = Account.objects.get(user=request.user)
            if account.is_active:
                error = ""
            else:
                logout(request)
                error = "Your account is not active."
            return HttpResponse(error)
        else:
            return HttpResponse(error)
    return render(request, template_name, contex)



def userCreate_view(request):
    next = request.GET.get('next', '/')
    if request.user.is_authenticated:
        return redirect(next)

    template_name = 'accounts/registration.html'
    contex = {}
    if request.method == "POST":
        name     	= request.POST['name']
        email    	= request.POST['email']
        password 	= request.POST['password']
        re_password = request.POST['re-password']
        errors      = registerValidation(name, email, password, re_password)
        if errors != "":
            contex = {'errors': errors}
        else:
            _name	 		= name.split()
            user    	    = User()
            user.first_name = _name[0]
            user.last_name  = ' '.join(_name[1:])
            user.username 	= usernameGenerator(email)
            user.email 		= email
            user.set_password(raw_password=password)
            user.save()
            account = Account()
            account.user = user
            account.save()
            # SEND EMAIL
            subject = "Account confirmation"
            body    = "Hello " + user.first_name + ", your account has been created successfully. We want to provide some recovery codes for you for future usage. Activation code: " + str(account.activation_code) + " Password recovery code: " + str(account.forgotpass_code) + " Account recovery code: " + str(account.recover_code) + ". Don't forget to save these codes. Thanks from FRIENDS community."
            try:
                send_mail(subject, body, settings.EMAIL_HOST_USER, [user.email], fail_silently=True)
                print("Email has been sent")
            except:
                pass
            msg = "Congrats! You are now registered. Please check your email to <a href='/accounts/activate/?email="+user.email+"' class='alert-link'>confirm</a> your account."
            messages.success(request, msg)
            return HttpResponseRedirect('/accounts/login/')
    return render(request, template_name, contex)
