from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.template.loader import get_template
from mysite.models import Mood, Post

# Create your views here.


def index(request, pid=None, del_pass=None):
	template = get_template('index.html')
	
	posts = Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
	moods = Mood.objects.all()
	
	try:
		user_id = request.GET['user_id']
		user_pass = request.GET['user_pass']
		ur_post = request.GET['user_post']
		ur_mood = request.GET['mood']
	except:
		user_id = None
		message = 'Please fill the required information if you want to post something...'
	
	if del_pass and pid:
		try:
			post = Post.objects.get(id=pid)
		except:
			post = None
			
		if post:
			if post.del_pass == del_pass:
				post.delete()
				message = 'deleted'
			elif post.del_pass == '':
				message = 'Please enter your password'
			else:
				message = 'wrong password'
	
	
		
	elif user_id != None:
		mood = Mood.objects.get(status=ur_mood)
		post = Post.objects.create(mood=mood, nickname=user_id, del_pass=user_pass, message=ur_post)
		post.save()
		message = 'Saved! Please don\' forget your password[{}]!, the post will be displayed after review'.format(user_pass)

	html = template.render(locals())
	return HttpResponse(html)

