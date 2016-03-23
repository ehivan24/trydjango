from django.shortcuts import render
from .forms import SignUpForm, ContactForm
from django.core.mail import send_mail
from django.conf import settings
from .models import SignUp


def home(request):
	if request.user.is_authenticated():

		title = 'Welcome:  %s' % (request.user)
		context = {
			"template_name" : title,

		}
	else:
		title = 'Welcome:  Unknown User'
		context = {
			"template_name" : title,

		}

	#if request.method == "POST":
	#	print request.POST
	
	form = SignUpForm(request.POST or None)

	context = {
		'title' : title,
		'form' : form
	}
	if form.is_valid():
		instance = form.save(commit=False)

		full_name = form.cleaned_data.get('full_name')
		if not full_name:
			full_name = 'Unknown'
		instance.full_name = full_name
		instance.save()
		#print instance.email
		#print instance.timestamp
		
		context = {
		'title' : 'Thank you !',
		
		}

	if request.user.is_authenticated() and request.user.is_staff:
		queryset = SignUp.objects.all().order_by('-timestamp')
		context = {
			"queryset" : queryset
		}

	return render(request,"home.html", context)

def contact(request):
	title = ' Some text to understand bootstrap! '
	form =  ContactForm(request.POST or None)
	if form.is_valid():
		#for key, value in form.cleaned_data.iteritems():
		#	print key, value
		email = form.cleaned_data.get('email')
		message = form.cleaned_data.get('message')
		full_name = form.cleaned_data.get('full_name')
		subject = 'Site Contact'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email , 'ehivan24@yahoo.com']
		contact_message = """
			%s %s via %s 
		""" % (full_name, message, email)

		send_mail(subject, 
				contact_message, 
				from_email, 
				to_email, 
				fail_silently=False)
		

			

	context = {
		'title': title,
		'form': form

	}
	return render(request,"forms.html", context)


