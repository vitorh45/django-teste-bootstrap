from django.shortcuts import render_to_response
from django.template import RequestContext
from posts.models import Category, Post

def index(request):
	posts_highlight = Post.objects.filter(is_highlight=True)
	posts = Post.objects.exclude(is_highlight=True)	
	return render_to_response('index.html',{
			'posts_highlight': posts_highlight,
			'posts': posts},context_instance=RequestContext(request))
