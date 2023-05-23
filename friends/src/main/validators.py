import re
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.models import User

def validUsername(username):
	message = ""
	if not re.compile("^[A-Za-z._]+$").match(username):
		message = "username contains invalid character(s)."
	if len(username) < 3:
		message = "username is too short."
	if len(username) > 32:
		message = "username is too large."

	return message

def validateName(name):
	message = ""
	if not re.compile("^[A-Za-z ._]+$").match(name):
		message = "<span>invalid character</span>"

	if len(name) < 3:
		message = "<span>too short</span>"
	return message

def validateEmail(email):
	message = ""
	try:
	    validate_email(email)
	except ValidationError as e:
	    message = 'invalid e-mail'

	# Already exists check
	qs = User.objects.filter(email=email)
	if qs.exists():
	    message = 'already exists'
	return message



def validateEmail_for_contect(email):
	message = True
	try:
	    validate_email(email)
	except ValidationError as e:
	    message = False
	return message

def registerValidation(name, email, password, re_password):
	errors = ""
	if validateName(name) != "":
		errors += "<li><strong>Name</strong>: "+validateName(name)+"</li>"
	if validateEmail(email) != "":
		errors += "<li><strong>E-mail</strong>: "+validateEmail(email)+"</li>"
	if len(password) < 6:
		errors += "<li><strong>Password</strong>: too short</li>"
	if password != re_password:
		errors += "<li><strong>Password</strong>: didn't match</li>"
		
	return errors