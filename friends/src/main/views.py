from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http import HttpResponse
from .validators import *
from posts.forms import postForm
from .models import Contact
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from notifications.models import Notification
from posts.models import Post
from comments.models import Comment


def search_view(request):
	template_name = 'search.html'
	query = ''
	if request.method == 'POST' and not request.is_ajax():
		query = request.POST.get('q', '')
		if query == '' or query == None:
			query = ''
	if request.is_ajax():
		query    = request.POST.get('query')
		posts    = Post.objects.search(query=query)
		comments = Comment.objects.search(query=query)
		data    = ""
		for post in posts:
			tmp   = "<li class='list-group-item search_res_hover p-2'>" + "<a href='"+ post.get_absolute_url +"' class='text-muted'>"+ post.content[:70] +"</a></li>"
			data += tmp
		for comment in comments:
			tmp   = "<li class='list-group-item search_res_hover p-2'>" + "<a href='"+ comment.post.get_absolute_url +"' class='text-muted'>"+ comment.content[:70] +"</a></li>"
			data += tmp
		if data == "":
			data = "<li class='list-group-item search_res_hover text-center p-2'>" + "<a href='#' class='text-danger'>No result matched!</a></li>"
		return HttpResponse(data)
	contex = {
		'query': query,
	}
	return render(request, template_name, contex)








def notificationStatus_view(request, pk):
	try:
		notification = Notification.objects.get(pk=pk)
		if not notification.is_seen:
			notification.is_seen = True
			notification.save()
	except:
		pass
	return redirect(notification.post.get_absolute_url)

@login_required
def notifications_view(request):
	template_name = 'notification.html'
	contex = {

	}
	return render(request, template_name, contex)

def contactUs_view(request):
	template_name = 'contact.html'
	error = ""
	if request.method == 'POST':
		name    = request.POST.get('name')
		email   = request.POST.get('email')
		subject = request.POST.get('subject')
		message = request.POST.get('message')
		if not name or not email or not subject or not message:
			error = "Please fill up all the fields. All fields are required."
		if len(name) == 0 or len(email) == 0 or len(subject) == 0 or len(message) == 0:
			error = "Please fill up all the fields. All fields are required."
		if not validateEmail_for_contect(email):
			error = "Email you entered is not a valid one."
		else:
			contact = Contact()
			contact.name = name
			contact.email = email
			contact.subject = subject
			contact.message = message
			contact.save()
			print(contact)
			error = "Thank you! You message has been sent successfully."
			messages.success(request, error)
			return HttpResponseRedirect('/contact-us/')
	contex = {
		'error': error
	}
	return render(request, template_name, contex)
def ErrorNotFound_view(request):
    template_name = '404.html'
    message = request.GET.get('message', None)
    contex = {
        'message': message
    }
    return render(request, template_name, contex)




def home_view(request):
    template_name = 'base.html'
    contex = {
		'form': postForm()
	}
    return render(request, template_name, context=contex)

def valildateName_view(request):
	if request.is_ajax() and request.method == 'POST':
		name = request.POST['data']
		return HttpResponse(validateName(name))
	return HttpResponse('')


def valildateEmail_view(request):
	if request.is_ajax() and request.method == 'POST':
		email = request.POST['data']
		return HttpResponse(validateEmail(email))
	return HttpResponse('')


def valildatePassword_view(request):
	if request.is_ajax() and request.method == 'POST':
		password = request.POST['data']
		if len(password) < 6:
			return HttpResponse("<span class='text-danger'>Too short</span>")
	return HttpResponse('')