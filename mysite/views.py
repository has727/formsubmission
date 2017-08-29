from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.template.loader import get_template

# Create your views here.


def index(request):
	template = get_template('index.html')
	try:
		urid = request.GET['user_id']
		urpass = request.GET['user_pass']
	except:
		urid = None
	
	if urid != None and urpass == '12345':
		verified = True
	else:
		verified = False
		
	years = range(1960, 2021)
	urfcolor = request.GET.getlist('fcolor')
	yearok = request.GET.getlist('byear')
	html = template.render(locals())
	return HttpResponse(html)

