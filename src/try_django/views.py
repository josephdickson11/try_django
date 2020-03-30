from django.http import HttpResponse



def home_page(request):
	return HttpResponse("<h1> hello world</h1>")
	pass

def about_page(request):
	return HttpResponse("<h1>about us</h1>")
	pass

def contact_page(request):
	return HttpResponse("<h1>contact us</h1>")
	pass